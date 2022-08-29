from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView
from django.db.models import Avg,Max,Min,Count,Sum
import logging
from django.core import serializers
from .forms import LoginForm, MyUserRegister, BuyItems, BalanceUpdate, BuyItemForm
from .models import Profile, Item, ShoppingCart, ProductReport
from django.db import transaction

logger = logging.getLogger(__name__)


@transaction.atomic
def buy_item(user_info):
    """
    Функция, которая совершает покупку товара, списывает баланс, и уменьшает количество товара на складе

    :param user_info: request.user
    :return: boolean
    """

    profile_user = Profile.objects.get(user_id=user_info.id)
    cart = ShoppingCart.objects.get(cart_user=profile_user)
    #Найдем все товары
    all_items = cart.items.all()
    price_all_itmes = 0
    #Текущий баланс пользователя
    user_balance = profile_user.balance
    #тут посчитаем сумму всех товаров в корзине
    for item in all_items:
        price_all_itmes += (item.price * item.count_pay)

    #тут проверим что баланс больше чем сумма всех товаров в корзине
    if user_balance < price_all_itmes:
        return False
    else:
        #Тут вычитаем количество каждого товара со склада
        for item in all_items:
            #Тут сначлао првоерим всем товары на количествои с клада
            if item.amount_item < item.count_pay:
               return False


        for item in all_items:
            # Добавим купленный товар в наш отчет личный отчет пользователя БД
                ProductReport.objects.create(
                    user_report=user_info,
                    id_product=item.id,
                    name=item.name,
                    description=item.description,
                    price=item.price,
                    count_pay=item.count_pay
                  )

                item.amount_item -= item.count_pay
                cart.items.remove(item)
                cart.save()
                item.save()



        #Вычтим с баланса
        profile_user.balance -= price_all_itmes
        logger.debug('У Пользователь {user}, уменьшился баланс на {balance}'.format(user=profile_user.user, balance=price_all_itmes))
        #добавим очки пользователю
        profile_user.score += price_all_itmes
        profile_user.save()

    logger.debug('Пользователь {user} успешно совершил покупку'.format(user=profile_user.user))

    return True


#функция проверки на авторизирвоаного пользователя
def check_user(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))


class MyLogoutView(LogoutView):
    """
      Представление с логаутом.
      """
    next_page = '/'  # или перенаправление сюда


class LoginView(View):
    """
    Представление с логированием пользователя.
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    logger.info('Залогинился пользователь {}'.format(username))
                    return HttpResponseRedirect(reverse('index'))

        form = LoginForm()
        return render(request, 'login.html', {'from': form})


class Mysort:
    def __init__(self, count, name, id):
        self.count = count
        self.name = name
        self.id = id

class MainIndex(View):
    """
    Представление главной страницы.
    """
    def get(self, request):

        logger.info('Запрошена главная страница через GET - ВЫВЕСТИ В КОСНОЛЬ')
        logger.debug('Запрошена главная страница через GET - ВЫВЕСТИ В ФАИЛ')

        #Запрос если там есть ключ ForeignKey ( select_related) или если ManyToManyField(prefetch_related)
        # Так же если нужно например что бы запросить 1 поля из БД а не все подряд используется .only('name'),
        # если нужно что бы еще при этом было еще какое то значение из связаной бд то через __ например blog__name (в ключе blog будет запрашиватсья только имя)
        # Пример
        # post= Post.objects.select_related('blog').only('title', 'blog__name')

        # format = request.GET['format']
        # if format not in ['xml', 'json']:
        #     return HttpResponseBadRequest()
        # else:
        #     data = serializers.serialize(format, ProductReport.objects.select_related('user_report').all())
        #     return HttpResponse(data)

        no_id = []
        total = []
        sort_total_x = []
        super_sort = []
        product_report = ProductReport.objects.select_related('user_report').all()
        for i in product_report:
            if i.id_product not in no_id:
                no_id.append(i.id_product)
                temp = ProductReport.objects.filter(id_product=i.id_product).aggregate(Total_count=Sum('count_pay'))
                total.append((temp.get('Total_count'), i.name, i.id_product))


        sort_total_x = sorted(total,  key=lambda x: x[0], reverse=True) [:5]
        for i in sort_total_x:
            super_sort.append(Mysort(i[0], i[1], i[2]))


        return render(request, 'index.html', {'product_report': product_report, 'super_sort': super_sort})


class Register(View):
    """
    Представления регистрации нового пользователя.
    """
    def get(self, request):
        form = MyUserRegister()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = MyUserRegister(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            gender = form.cleaned_data.get('gender')
            avatar = form.cleaned_data.get('avatar')
            phone = form.cleaned_data.get('phone')
            # тут сохраним дополнительные параметры юзера
            my_profile = Profile.objects.create(
                user=user,
                gender=gender,
                avatar=avatar,
                phone=phone
            )
            my_profile.save()
            #получим данные логин и пароль валидные
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #Привяжем корзину сразу
            ShoppingCart.objects.create(cart_user=my_profile)
            #Залогинимся сразу после регистрации
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logger.debug('Появился новый пользователь {}'.format(username))
            return HttpResponseRedirect(reverse('index'))

        form = MyUserRegister(instance=request.user)
        return render(request, 'register.html', {'form': form})


class ItemList(ListView):
    """
    Представление со списком товаров.
    """
    model = Item
    template_name = 'items_list.html'
    context_object_name = 'item_list'
    queryset = Item.objects.prefetch_related('shops').all()


class ItemListDetail(View):

    def get(self, request, pk):
        add_cart = BuyItems()
        detail_items = Item.objects.prefetch_related('shops').get(pk=pk)
        if detail_items.amount_item > 0:
            is_active = True
        else:
            is_active = False

        return render(request, 'items_list_detail.html', {'detail_items': detail_items, 'add_cart': add_cart, 'is_active': is_active})

    def post(self, request, pk):
        add_cart = BuyItems(request.POST)
        detail_items = Item.objects.get(pk=pk)
        if detail_items.amount_item > 0:
            is_active = True
        else:
            is_active = False


        if add_cart.is_valid():
            id_item = add_cart.cleaned_data.get('id_item')
            count_item = add_cart.cleaned_data.get('count_item')

            #найдем наш товар
            item = Item.objects.get(id=id_item)
            item.count_pay = count_item
            item.save()

            #Так же найдем профиль нашего пользователя
            profile_user = Profile.objects.get(user_id=request.user.id)
            cart = ShoppingCart.objects.get(cart_user=profile_user)
            cart.items.add(item)
            cart.save()
            return HttpResponseRedirect(reverse('items_list'))

        return render(request, 'items_list_detail.html', {'detail_items': detail_items, 'add_cart': add_cart, 'is_active': is_active})


class ProfileInfo(View):

    def get(self, request):
        form_buy = BuyItemForm()
        check_user(request)
        user_info = request.user
        profile_user = Profile.objects.get(user_id=user_info.id)
        product_report = ProductReport.objects.select_related('user_report').filter(user_report=user_info)

        #Проверка статуса пользователя
        if 100 <= profile_user.score < 1000:
            profile_user.status_profile = 'продвинутый'
            logger.debug('Пользователь {user} успешно изменил статус на "продвинутый"'.format(user=profile_user.user))
            profile_user.save()
        elif 1000 <= profile_user.score < 10000:
            profile_user.status_profile = 'эксперт'
            logger.debug('Пользователь {user} успешно изменил статус на "эксперт"'.format(user=profile_user.user))
            profile_user.save()
        elif profile_user.score >= 10000:
            profile_user.status_profile = 'БОГ покупок'
            logger.debug('Пользователь {user} успешно изменил статус на "БОГ покупок"'.format(user=profile_user.user))
            profile_user.save()

        if profile_user.avatar == '':
            avatar_checked = False
        else:
            avatar_checked = True


        return render(request, 'profile_info.html', {'profile_user': profile_user,  'form_buy': form_buy, 'product_report': product_report, 'avatar_checked': avatar_checked})


class BalanceUp(View):
    def get(self, request):
        form = BalanceUpdate()
        return render(request, 'balance_up.html', {'form': form})

    def post(self, request):
        form = BalanceUpdate(request.POST)
        if form.is_valid():
            prof = Profile.objects.get(user_id=request.user.id)
            money = form.cleaned_data.get('money')
            #баланс
            prof.balance += money
            prof.save()
            logger.debug('Пользователь {user}, пополнил баланс на {balance}'.format(user=prof.user, balance=prof.balance))
            return HttpResponseRedirect(reverse('profile_info'))

        form = BalanceUpdate()
        return render(request, 'balance_up.html', {'form': form})

class ShopingCartView(View):

    def get(self, request):
        form_buy = BuyItemForm()
        check_user(request)
        user_info = request.user
        profile_user = Profile.objects.get(user_id=user_info.id)
        if ShoppingCart.objects.all():
            cart = ShoppingCart.objects.get(cart_user=profile_user)
            all_items = cart.items.all()
            price_all_itmes = 0
            # тут посчитаем сумму всех товаров в корзине
            for item in all_items:
                price_all_itmes += (item.price * item.count_pay)
        else:
            cart = False
            price_all_itmes = 0

        error_messages = ''

        return render(request, 'shopping_cart.html', {'profile_user': profile_user, 'cart': cart, 'form_buy': form_buy,
                                                     'price_all_itmes': price_all_itmes, 'error_messages': error_messages})

    def post(self, request):
        error_messages = ''
        form_buy = BuyItemForm(request.POST)
        user_info = request.user
        profile_user = Profile.objects.get(user_id=user_info.id)
        cart = ShoppingCart.objects.get(cart_user=profile_user)
        all_items = cart.items.all()
        price_all_itmes = 0
        # тут посчитаем сумму всех товаров в корзине
        for item in all_items:
            price_all_itmes += (item.price * item.count_pay)
        if form_buy.is_valid():

            if (buy_item(user_info)):
                error_messages = 'Спасибо за покупку!'
                price_all_itmes = 0
            else:
                error_messages = 'Ошибка покупки'

        return render(request, 'shopping_cart.html', {'profile_user': profile_user, 'cart': cart, 'form_buy': form_buy,
                                                     'price_all_itmes': price_all_itmes, 'error_messages': error_messages})
