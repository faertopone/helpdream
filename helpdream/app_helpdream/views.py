from datetime import timedelta
import random

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
import requests
from django.db.models import Sum
from django.contrib.auth.views import PasswordResetView, PasswordContextMixin, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

from .forms import MyUserRegister, BalanceUp, WriteDreamForm, EditDreamForm, RestorePasswordForm, CommentForm, \
    HelpAmount, FullInfoUser, EditUserForm, EditUserPasswordForm, FeedbackForm, PopolnenieBoxDream, \
    CustomPasswordResetForm, LoginForm, CustomePasswordResetConfirmForm, FilterForm

from .models import Profile, WriteDeam, ImgWriteDream, Comments, WhoHelpMe, TotalBoxDream, HistoryBoxDream, WinDream, \
    WhoHelpMeBoxDream
from django.db import transaction
import logging

from django.conf import settings



logger = logging.getLogger(__name__)

# Сумма при которой будет розыгрыщ боксдрим
BOX_DRAW_PRICE = 100000
# Сколько нужно активных обьявления размещения для розыгрыша
BOX_DRAW_DREAM = 5
# ограничем максимальную сумму на мечту при распределения выйгрыша
MAX_BOX_WIN_ONE_DREAM = 50000

MY_EMAIL = 'Sergey-kolyhalov@rambler.ru'

#=============================== ВСПОМОГАТЕЛЬНЫЕ ФУНЦИИ===============================================

#Перезапсиывает номер по порядку)
def sort_count(qerset):
    place = 1
    for i in qerset:
        i.place = place
        place += 1
        i.save()


# Функция которая в БД запишет истоия розыгрыша
def create_history_win_dream(win_dream, current_history_draw, need_help_dream):
    # Созаддим модель кому какой мечте помогли и на сколько
    win_dream_item = WinDream.objects.create(amount_help_box=need_help_dream,
                                             who_dream_box=win_dream)
    # Это модель нужна что бы потмо отображать кто помог мечте
    who_help_box = WhoHelpMeBoxDream.objects.create(box_win_price=need_help_dream)
    win_dream.where_dream_box.add(who_help_box)
    win_dream.save()

    # А тут добавим эту модель в списко истории для этого розыгрыша
    current_history_draw.win_dream.add(win_dream_item)


# Функция алгоритма розыгрыша
def boxdreamdraw(total_balanc_box, active_dreams):
    """
    ФФункция,где после пополения BOXDREAM и выполенния условий будет розыгрыш среди других мечт
    :param total_balanc_box: querset
    :return: none
    """

    global MAX_BOX_WIN_ONE_DREAM

    # Созаддим в БД модель эжтого розыгрыша
    current_history_draw = HistoryBoxDream.objects.create(count_win=total_balanc_box.count_win_box)
    # ПОтмо увеличим для след розыгрыша номер
    total_balanc_box.count_win_box += 1
    total_balanc_box.save()

    #Сначала присвоим каждой мечто свой номер
    number_dream = 0
    max_number_win = active_dreams.count()
    for i_dream in active_dreams:
        i_dream.number_for_draw = number_dream
        i_dream.save()

        number_dream += 1
    flag_draw = True
    win_list = []
    # Будем разыгрывать пока не кончатсья деньги или мечты)
    while(flag_draw):

        win_number = random.randint(0, max_number_win - 1)
        if win_number not in win_list:
            win_list.append(win_number)
            win_dream = active_dreams.get(number_for_draw=win_number)

            # Находим сколько осталось собрать -) из сколько хотели вычитаем сколько уже собрали
            need_help_dream = win_dream.price - win_dream.help_price

            # Если не обходимая сумма больше ограничения - сделаем ее ограниченной
            if need_help_dream >= MAX_BOX_WIN_ONE_DREAM:
                need_help_dream = MAX_BOX_WIN_ONE_DREAM


            if need_help_dream <= total_balanc_box.balance:
                # Спишем эту сумму с баланса
                total_balanc_box.balance -= need_help_dream
                # Прибавим эту сумму к мечте
                win_dream.help_price += need_help_dream
                # Вызовим функцию создадиня в БД отчета поэтому дейтсвию
                create_history_win_dream(win_dream, current_history_draw, need_help_dream)
            else:
                # Если сумма на балансе меньше чем требуется мечте, все перечислм тогда
                win_dream.help_price += total_balanc_box.balance
                # Вызовим функцию создадиня в БД отчета поэтому дейтсвию
                create_history_win_dream(win_dream, current_history_draw, total_balanc_box.balance)
                total_balanc_box.balance = 0

            # Проверим мечту сколько собрали) если собрали то делаем завершенной
            if win_dream.help_price >= win_dream.price:
                # Изменим статус мечты на выполнено
                win_dream.dream_is_active = False
                win_dream.dream_is_complete = True

            # Сохарним изменения для этой мечты
            win_dream.save()
            total_balanc_box.save()

        #Завершенеи розыгрыша если кончились мечты или баланс 0
        if len(win_list) == max_number_win or total_balanc_box.balance == 0:
            flag_draw = False

    logger.info('Закончили цикл розыгрыша')


def dream_checked(user_dream):
    """
    Фильтрует мечты и делате порядок
    :param user_dream: qyerset
    :return:
    """
    # активные мечты
    active_dream = user_dream.filter(dream_is_active=True).order_by('creadet_at_dream')
    sort_count(active_dream)

    # завершенные мечты
    complete_dream = user_dream.filter(dream_is_complete=True).order_by('creadet_at_dream')
    sort_count(complete_dream)

    # Мечты которые отменили
    wait_dream = user_dream.filter(dream_is_active=False, dream_is_complete=False).order_by('creadet_at_dream')
    sort_count(wait_dream)

    return (active_dream, complete_dream, wait_dream)

# Функция проведения оплаты
def pay_bank(amount, profile):
    return True
    # Тут оплаты - запись данных в БД запись успешного проведения операции и из какого банка и тд и тп

# Функция пополения - оплаты в личном кабинете
def help_balance_up(amount, profile):
    # На всякий случай проверю что там не None
    if amount != None:
        profile.my_balance += amount
        profile.save()


# Атомик что бы все выполнилось одновремено
@transaction.atomic
def purchase(amount, profile):
    flag_compelete = False
    #Вызовим функцию оплаты
    flag_pay_bank = pay_bank(amount=amount, profile=profile)
    # Вызовим функцию для внесения данных в БД
    help_balance_up(amount=amount, profile=profile)
    if flag_pay_bank:
        flag_compelete = True

    return flag_compelete

# Атомик что бы все выполнилось одновремено
@transaction.atomic
def popolneni_boxdream(author, amount_box):
    """
    Функция которая выполнеит пополенения BOXDREAM  и если соберем нужную сумму и будут активные мечты выполним розыгрыш
    функцией boxdreamdraw(box_dream, activ_dreams)
    :param author:
    :param amount_box:
    :return:
    """

    global BOX_DRAW_PRICE
    global BOX_DRAW_DREAM

    float_draw = False
    # Вычтим с баланса профиля
    author.my_balance -= amount_box
    # добавим баллы к помощи
    author.help_balanced += amount_box
    author.save()
    help_balance_user = author.help_balanced
    check_balance_rank(help_balance_user, author)
    # запишем в модель кто помог (сумма и профиль)
    who_help = WhoHelpMe.objects.create(who_price=amount_box,
                             help_profile=author)

    # Добавим в наш общий баланс бокхдрим - он создается в мидлевайр -если не был создан
    box_dream = TotalBoxDream.objects.prefetch_related('who_help_boxdream').get(id=1)

    box_dream.balance += amount_box
    box_dream.who_help_boxdream.add(who_help)
    box_dream.save()

    logger.info('Попалли в йункцию popolneni_boxdream')
    activ_dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True)
    print(activ_dreams)
    if box_dream.balance >= BOX_DRAW_PRICE and activ_dreams.count() >= BOX_DRAW_DREAM:
        #тут если условия верны вызовем функцию где разыграем эту сумму
        logger.info('вызываем функцию boxdreamdraw')
        boxdreamdraw(box_dream, activ_dreams)
        #Знаичт был роызгырш
        float_draw = True
        return float_draw
    # Знаичт не было розыгрыша
    return float_draw

#==================================================================================================


def check_balance_rank(help_balance_user, profile_user):

     if profile_user.rank != 5:
        if help_balance_user >= 100000:
            profile_user.rank = 5

        elif help_balance_user >= 30000:
            profile_user.rank = 4

        elif help_balance_user >= 10000:
            profile_user.rank = 3

        elif help_balance_user >= 1000:
            profile_user.rank = 2

        elif help_balance_user >= 100:
            profile_user.rank = 1

        # Изменения статуса аватарки, и другие возмоджности профиля относительно вашего ранга
        profile_user.img = profile_user.choise_rank()
        profile_user.save()


# Функция перевода баланса нужному пользователю
# Атомик что бы все выполнилось одновремено
@transaction.atomic
def balance_transfer(messages_text, amount, profile_user, dream_items):
    """
    Функция перевода баланса баллов нужному пользователю
    :param messages_text: str
    :param amount: integer
    :param profile_user: querset
    :param dream_items: querset
    :return: none
    """
    # Заполним БД данными
    who_help = WhoHelpMe.objects.create(messages=messages_text,
                                         who_price=amount,
                                         help_profile=profile_user
                                         )
    # Прибавим на сколько помогли
    dream_items.help_price += amount
    # Отнимем эту сумму у пользователя
    profile_user.my_balance -= amount

    # Проверим хватит ли этого на завершение мечты
    if dream_items.help_price >= dream_items.price:
        dream_items.dream_is_active = False
        dream_items.dream_is_complete = True

    # Добавим данные на сколько пользователь помог
    profile_user.help_balanced += amount
    help_balance_user = profile_user.help_balanced
    # Теперь првоерим на сколько помогли и присвоим нужный ранг
    check_balance_rank(help_balance_user, profile_user)

    # Добавим в мечту инфу кто помог
    dream_items.where_dream.add(who_help)



    # Сохраним изменения
    profile_user.save()
    dream_items.save()

#===============================  КОНЕЦ ВСПОМОГАТЕЛЬНЫХ ФУНКЦИЙ ===============================================


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class IndexView(View):

    def get(self, request):

        boxdream = TotalBoxDream.objects.get(id=1)
        flag_dream = False
        need_count_active_dream = 0
        activ_dreams_count = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).count()
        Leftbeforethedraw = 100000 - boxdream.balance
        if Leftbeforethedraw <= 0:
            Leftbeforethedraw = 0
            if activ_dreams_count < BOX_DRAW_DREAM:
                need_count_active_dream = BOX_DRAW_DREAM - activ_dreams_count
                flag_dream = True


        return render(request, 'index.html', {'boxdream': boxdream,
                                              'Leftbeforethedraw': Leftbeforethedraw,
                                              'flag_dream': flag_dream,
                                              'need_count_active_dream': need_count_active_dream})


class LoginView(View):

    def get(self, request):
        error_login_flag = False
        form = LoginForm()

        return render(request, 'authorization.html', {'form': form, 'error_login_flag': error_login_flag})

    def post(self, request):
        error_login_flag = False
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('user_lk'))
            else:
                error_login_flag = True
        form = LoginForm()

        return render(request, 'authorization.html', {'form': form, 'error_login_flag': error_login_flag})


class RegisterView(View):

    def get(self, request):
        form = MyUserRegister()

        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = MyUserRegister(request.POST, request.FILES)
        if form.is_valid():
            # СОхраним данные юзера
            user = form.save()

            profile_user = Profile.objects.create(
                user=user,
            )
            profile_user.save()
            #===================================


            # далее сразу залогинимся
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('user_lk'))


        return render(request, 'register.html', {'form': form})


class UserLkView(View):

    def get(self, request):

        if request.user.is_superuser:
            return HttpResponseRedirect('/admin/')
        if not request.user.is_authenticated:
            return redirect('index')

        user_lk = Profile.objects.get(user=request.user)
        form_dop_info = FullInfoUser()
        form_balance_up = BalanceUp()
        # Форма обработки кнопок редактирвоания созданых мечт
        form_dream_edit = EditDreamForm()
        # Мечты этого пользователя
        user_dream = WriteDeam.objects.filter(who_dream=user_lk)
        # Разрешение на создание мечт
        permission_dream = False
        if user_dream.filter(dream_is_active=True).count() < user_lk.max_dream_created:
            permission_dream = True

        #Тут фильтрует мечты
        filter_dream = dream_checked(user_dream)
        # заполним переменными после фильтрации
        active_dream = filter_dream[0]
        complete_dream = filter_dream[1]
        wait_dream = filter_dream[2]

        return render(request, 'user_lk.html', {'user_lk': user_lk,
                                                'form_balance_up': form_balance_up,
                                                'active_dream': active_dream,
                                                'complete_dream': complete_dream,
                                                'wait_dream': wait_dream,
                                                'form_dream_edit': form_dream_edit,
                                                'permission_dream': permission_dream,
                                                'form_dop_info': form_dop_info
                                                })


    def post(self, request):
        user_lk = Profile.objects.get(user=request.user)

        #Форма обработки кнопок редактирвоания созданых мечт
        form_dream_edit = EditDreamForm(request.POST)
        form_dop_info = FullInfoUser(request.POST, request.FILES)

        #обработка формы с дополненеим информации о себе
        if form_dop_info.is_valid():
            user_lk.avatar = form_dop_info.cleaned_data.get('avatar')
            user_lk.gender = form_dop_info.cleaned_data.get('gender')
            my_user = User.objects.get(id=request.user.id)
            my_user.first_name = form_dop_info.cleaned_data.get('first_name')
            my_user.save()
            user_lk.phone = form_dop_info.cleaned_data.get('phone')

            #Вычисления сегоднешней даты
            dt_now = datetime.now()
            dt_now_str = dt_now.strftime("%d/%m/%y")
            dt_now_obj = datetime.strptime(dt_now_str, "%d/%m/%y")


            input_birthday = form_dop_info.cleaned_data.get('birthday')
            input_birthday_str = input_birthday.strftime("%d/%m/%y")
            input_birthday_obj = datetime.strptime(input_birthday_str, "%d/%m/%y")
            user_lk.birthday = input_birthday_obj
            age = dt_now_obj.year - input_birthday_obj.year
            user_lk.age = age

            if user_lk.rank == 0:
                user_lk.rank = 1
                user_lk.img = user_lk.choise_rank()

            user_lk.all_info_user = True
            user_lk.save()

        # Обработки действий что делатьс мечстой - удалить, активирвоатьи тд и тп
        if form_dream_edit.is_valid():
            id_dream = form_dream_edit.cleaned_data.get('id_dream')
            push_up = form_dream_edit.cleaned_data.get('push_up')
            cancel = form_dream_edit.cleaned_data.get('cancel')
            active = form_dream_edit.cleaned_data.get('active')
            delete = form_dream_edit.cleaned_data.get('delete')
            if active:
                dream = WriteDeam.objects.get(id=id_dream)
                dream.dream_is_active = True
                dream.save()
            elif cancel:
                dream = WriteDeam.objects.get(id=id_dream)
                dream.dream_is_active = False
                dream.save()
            elif push_up:
                dream = WriteDeam.objects.get(id=id_dream)
                dream.creadet_at_dream = dream.updated_dream
                dream.save()
            elif delete:
                dream = WriteDeam.objects.get(id=id_dream)
                #Деньги которые собрали перейдут в баланс профиля
                user_lk.my_balance += dream.help_price * 0.9
                dream.delete()

        # Мечты этого пользователя
        user_dream = WriteDeam.objects.filter(who_dream=user_lk)
        #Разрешение на создание мечт
        permission_dream = False
        if user_dream.filter(dream_is_active=True).count() < user_lk.max_dream_created:
            permission_dream = True

        # Тут фильтрует мечты
        filter_dream = dream_checked(user_dream)
        active_dream = filter_dream[0]
        complete_dream = filter_dream[1]
        wait_dream = filter_dream[2]

        #Пополнение баланса
        form_balance_up = BalanceUp(request.POST)

        if form_balance_up.is_valid():
            amount = form_balance_up.cleaned_data.get('balance')
            logger.info('Оплата валидна')
            #Вызовем функции для пополенния баланса
            if purchase(amount, user_lk):
                # Успешно все прошло
                return redirect('operation_ok')
            return redirect('operation_errors')

        return render(request, 'user_lk.html', {'user_lk': user_lk,
                                                'form_balance_up': form_balance_up,
                                                'active_dream': active_dream,
                                                'complete_dream': complete_dream,
                                                'wait_dream': wait_dream,
                                                'form_dream_edit': form_dream_edit,
                                                'permission_dream': permission_dream,
                                                'form_dop_info': form_dop_info
                                                })

# Не использую )
class RestorePasswordView(View):

    def get(self, request):

        form = RestorePasswordForm()

        return render(request, 'restore_password.html', {'form': form})

    # def post(self, request):
    #     form = RestorePasswordForm(request.POST)
    #     if form.is_valid():
    #         send_mail(
    #             subject='ЗАГОЛОВОК',
    #             message='TEXT',
    #             from_email='Автор письма кто отпарвит',
    #             #Кому отправить
    #             recipient_list=[form.cleaned_data.get('email')]
    #         )
    #         return HttpResponseRedirect(reverse('index'))
    #
    #     return render(request, 'restore_password.html', {'form': form})


class WriteDreamView(View):


    def get(self, request):

        if request.user.is_superuser:
            return HttpResponseRedirect('/admin/')

        form = WriteDreamForm()
        current_user = request.user
        if current_user and current_user.is_authenticated:
            profile_user = Profile.objects.select_related('user').get(user=current_user)
        else:
            profile_user = False

        return render(request, 'write-dream.html', {'form': form,
                                                    'profile_user': profile_user})

    def post(self, request):
        current_user = request.user

        if current_user and current_user.is_authenticated:
            profile_user = Profile.objects.select_related('user').get(user=current_user)
        else:
            profile_user = False
            return redirect('writedream')

        # Мечты этого пользователя
        user_dream = WriteDeam.objects.select_related('who_dream').filter(who_dream=profile_user)
        form = WriteDreamForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            if price > profile_user.max_dream_price:
                return redirect('writedream')

            #Это если создано больше чем надо, мечту записываем в состояние ожидание
            if user_dream.filter(dream_is_active=True).count() < profile_user.max_dream_created:
                dream_is_active_x = True
            else:
                dream_is_active_x = False

            #Тут запишем в БД наши данные
            write_dream = WriteDeam.objects.create(
                who_dream=profile_user,
                title=title,
                description=description,
                price=price,
                dream_is_active=dream_is_active_x
            )

            write_dream.creadet_at_dream_time += timedelta(days=30)
            write_dream.save()

            imgs_dreams = request.FILES.getlist('imgs')
            #Сохраним фото к этой мечте
            for f_img in imgs_dreams:
                ImgWriteDream(img_dream=write_dream, img=f_img).save()

            return HttpResponseRedirect(reverse('user_lk'))



        return render(request, 'write-dream.html', {'form': form,
                                                    'profile_user': profile_user,
                                                    })


class OtherDreamView(View):

    def get(self, request):

        dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('-creadet_at_dream')
        paginator = Paginator(dreams, 100)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        all_dreams = paginator.get_page(page_number)
        filter_form = FilterForm()


        return render(request, 'other_dreams.html', {'all_dreams': all_dreams,
                                                     'filter_form': filter_form
                                                     })

    def post(self, request):
        filter_form = FilterForm(request.POST)

        dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('-creadet_at_dream')

        # Сортировка после фильтра
        if filter_form.is_valid():
            filter_param = filter_form.cleaned_data.get('filter_atr')
            if filter_param == '2':
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('creadet_at_dream')
            elif filter_param == '3':
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('help_price')
            elif filter_param == '4':
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('-help_price')
            elif filter_param == '5':
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('-price')
            elif filter_param == '6':
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('price')
            else:
                dreams = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).order_by('-creadet_at_dream')


        paginator = Paginator(dreams, 100)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        all_dreams = paginator.get_page(page_number)


        return render(request, 'other_dreams.html', {'all_dreams': all_dreams,
                                                    'filter_form': filter_form,
                                                     })


class DetailDreamView(View):

    def get(self, request, pk):
        user_info = request.user
        if user_info.is_authenticated and not user_info.is_superuser:
            author = Profile.objects.select_related('user').get(user=request.user)
            max_price_author = author.my_balance
        else:
            max_price_author = None

        form_comment = CommentForm()
        dream_items = WriteDeam.objects.select_related('who_dream').prefetch_related('comments').prefetch_related('where_dream').get(pk=pk)
        photo_dream = ImgWriteDream.objects.select_related('img_dream').filter(img_dream=dream_items)
        help_users = dream_items.where_dream.all()
        form_help_amount = HelpAmount(initial={'my_user_id': request.user.id})

        return render(request, 'dream_detail.html', {'dream_items': dream_items,
                                                     'photo_dream': photo_dream,
                                                     'help_users': help_users,
                                                     'form_comment': form_comment,
                                                     'form_help_amount': form_help_amount
                                                     })

    def post(self, request, pk):

        form_comment = CommentForm(request.POST)
        form_help_amount = HelpAmount(request.POST, initial={'my_user_id': request.user.id})
        dream_items = WriteDeam.objects.select_related('who_dream').prefetch_related('comments').prefetch_related('where_dream').get(pk=pk)
        photo_dream = ImgWriteDream.objects.select_related('img_dream').filter(img_dream=dream_items)
        help_users = dream_items.where_dream.all()

        if form_comment.is_valid():
            messages = form_comment.cleaned_data.get('messages')
            # Автор комментария
            author = Profile.objects.select_related('user').get(user=request.user)

            # Создали коментарий в БД
            item_comment = Comments.objects.create(messages=messages, author=author)
            # Добавим модель этого комментария в модель мечты
            dream_items.comments.add(item_comment)
            item_comment.save()
            form_comment = CommentForm()
            form_help_amount = HelpAmount(initial={'my_user_id': request.user.id})



        if form_help_amount.is_valid():
            profile_user = Profile.objects.select_related('user').get(user=request.user)
            messages_text = form_help_amount.cleaned_data.get('messages_text')
            amount = form_help_amount.cleaned_data.get('amount')
            #Вызовем функцию где будем записсыватьв БД эти данные
            balance_transfer(messages_text, amount, profile_user, dream_items)

            dream_items = WriteDeam.objects.select_related('who_dream').prefetch_related('comments').prefetch_related(
                'where_dream').get(pk=pk)
            form_help_amount = HelpAmount(initial={'my_user_id': request.user.id})



        return render(request, 'dream_detail.html', {'dream_items': dream_items,
                                                     'photo_dream': photo_dream,
                                                     'help_users': help_users,
                                                     'form_comment': form_comment,
                                                     'form_help_amount': form_help_amount
                                                     })


class CompleteDreamsView(View):

    def get(self, request):

        filter_form = FilterForm()
        complete_dream = WriteDeam.objects.select_related('who_dream').prefetch_related('where_dream').filter(
            dream_is_complete=True).order_by('-updated_dream')

        #в этом цикле просто прсиваиваю порядковый номер, потом в HTML ильтрую первые MAX_PROFILE пользователей
        for x in complete_dream:
            place = 0
            for i in x.where_dream.all():
                i.place_number = place
                i.save()
                place += 1
        # Сколько выводить в заверешнной мечте, людей кто помог
        MAX_PROFILE = 4

        paginator = Paginator(complete_dream, 100)  # Show 30 contacts per page.
        page_number = request.GET.get('page')
        complete_dreams = paginator.get_page(page_number)

        return render(request, 'complete_dreams.html', {'complete_dreams': complete_dreams,
                                                        'MAX_PROFILE': MAX_PROFILE,
                                                        'filter_form': filter_form,
                                                        })


    def post(self, request):

        filter_form = FilterForm(request.POST)
        complete_dream = WriteDeam.objects.select_related('who_dream').prefetch_related('where_dream').filter(
            dream_is_complete=True).order_by('-updated_dream')
        # Сортировка после фильтра
        if filter_form.is_valid():
            filter_param = filter_form.cleaned_data.get('filter_atr')
            if filter_param == '2':
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    'creadet_at_dream')
            elif filter_param == '3':
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    'help_price')
            elif filter_param == '4':
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    '-help_price')
            elif filter_param == '5':
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    'price')
            elif filter_param == '6':
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    '-price')
            else:
                complete_dream = WriteDeam.objects.select_related('who_dream').filter(dream_is_complete=True).order_by(
                    '-creadet_at_dream')

        # в этом цикле просто прсиваиваю порядковый номер, потом в HTML ильтрую первые MAX_PROFILE пользователей
        for x in complete_dream:
            place = 0
            for i in x.where_dream.all():
                i.place_number = place
                i.save()
                place += 1
        # Сколько выводить в заверешнной мечте, людей кто помог
        MAX_PROFILE = 4

        paginator = Paginator(complete_dream, 100)  # Show 30 contacts per page.
        page_number = request.GET.get('page')
        complete_dreams = paginator.get_page(page_number)

        return render(request, 'complete_dreams.html', {'complete_dreams': complete_dreams,
                                                        'MAX_PROFILE': MAX_PROFILE,
                                                        'filter_form': filter_form,})



class TOPHumansView(View):

    def get(self, request):

        all_users = Profile.objects.select_related('user').all().order_by('-help_balanced')
        paginator = Paginator(all_users, 100)  # Show 100 contacts per page.
        page_number = request.GET.get('page')
        all_user = paginator.get_page(page_number)

        rank = 1

        for i in all_users:
            i.place = rank
            rank += 1
            i.save()


        return render(request, 'top.html', {'all_user': all_user})


class EditProfile(View):

    def get(self, request, pk):

        profile = Profile.objects.select_related('user').get(pk=pk)
        init_login = {
            'username': profile.user.username,
            'first_name': profile.user.first_name,
            'email': profile.user.email,
            'phone': profile.phone,
            'gender': profile.gender
        }
        form_password = EditUserPasswordForm(initial={'profile_id': profile.id})
        form = EditUserForm(initial=init_login)

        return render(request, 'edit_profile.html', {'form': form,
                                                     'form_password': form_password})


    def post(self, request, pk):

        profile = Profile.objects.select_related('user').get(pk=pk)
        form = EditUserForm(request.POST, request.FILES)
        form_password = EditUserPasswordForm(request.POST)
        init_login = {
            'username': profile.user.username,
            'first_name': profile.user.first_name,
            'email': profile.user.email,
            'phone': profile.phone,
            'gender': profile.gender
        }
        # Редактирование данных
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            gender = form.cleaned_data.get('gender')
            new_ava = form.cleaned_data.get('avatar')
            if new_ava:
                profile.avatar = new_ava
            profile.user.username = username
            profile.user.first_name = first_name
            profile.user.email = email
            profile.gender = gender
            profile.user.save()
            profile.save()
            return HttpResponseRedirect(reverse('user_lk'))

        # Изменение пароля
        if form_password.is_valid():
            password1 = form_password.cleaned_data.get('password1')
            profile.user.set_password(password1)
            profile.user.save()
            user = authenticate(username=profile.user.username, password=password1)
            login(request, user)
            return HttpResponseRedirect(reverse('user_lk'))

        form_password = EditUserPasswordForm(initial={'profile_id': profile.id})
        form = EditUserForm(initial=init_login)

        return render(request, 'edit_profile.html', {'form': form,
                                                     'form_password': form_password})


class AboutView(View):

    def get(self, request):

        form = FeedbackForm()

        return render(request, 'about.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            messeges_text = 'Сообщение написал ' + name + '\n' + 'Текст сообщения: ' + text

            send_mail(subject='Отзыв от {name}, его почта {mail}'.format(name=name, mail=email),
                      message=messeges_text,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[MY_EMAIL, settings.EMAIL_HOST_USER],
                      fail_silently=True)

            send_mail(subject='Ваш отзыв принят',
                      message='Спасибо за отзыв, мы обезательно его прочитаем и ответим Вам!',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[email],
                      fail_silently=True)

            return redirect('messagesgood')


        form = FeedbackForm()

        return render(request, 'about.html', {'form': form})


class BoxDreamView(View):

    def get(self, request):
        user_info = request.user

        if user_info.is_authenticated and not user_info.is_superuser:
            author = Profile.objects.select_related('user').get(user=request.user)
            author_my_balance = author.my_balance
        else:
            author_my_balance = None

        boxdream = TotalBoxDream.objects.get(id=1)
        boxdream_profiles = boxdream.who_help_boxdream.all()
        paginator = Paginator(boxdream_profiles, 10)  # Show 10 contacts per page.
        page_number = request.GET.get('page')
        boxdream_profiles = paginator.get_page(page_number)

        flag_dream = False
        need_count_active_dream = 0
        activ_dreams_count = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).count()
        Leftbeforethedraw = 100000 - boxdream.balance
        if Leftbeforethedraw <= 0:
            Leftbeforethedraw = 0
            if activ_dreams_count < BOX_DRAW_DREAM:
                need_count_active_dream = BOX_DRAW_DREAM - activ_dreams_count
                flag_dream = True
        form = PopolnenieBoxDream(initial={'max_balance_user': author_my_balance})

        return render(request, 'boxdream.html', {'form': form,
                                                 'boxdream': boxdream,
                                                 'boxdream_profiles': boxdream_profiles,
                                                 'Leftbeforethedraw': Leftbeforethedraw,
                                                 'need_count_active_dream': need_count_active_dream,
                                                 'flag_dream': flag_dream})


    def post(self, request):

        author = Profile.objects.select_related('user').get(user=request.user)
        form = PopolnenieBoxDream(request.POST, initial={'max_balance_user': author.my_balance})
        boxdream = TotalBoxDream.objects.get(id=1)
        boxdream_profiles = boxdream.who_help_boxdream.all()
        paginator = Paginator(boxdream_profiles, 10)  # Show 10 contacts per page.
        page_number = request.GET.get('page')
        boxdream_profiles = paginator.get_page(page_number)

        flag_dream = False
        need_count_active_dream = 0
        activ_dreams_count = WriteDeam.objects.select_related('who_dream').filter(dream_is_active=True).count()
        Leftbeforethedraw = 100000 - boxdream.balance
        if Leftbeforethedraw <= 0:
            Leftbeforethedraw = 0
            if activ_dreams_count < BOX_DRAW_DREAM:
                need_count_active_dream = BOX_DRAW_DREAM - activ_dreams_count
                flag_dream = True

        if form.is_valid():
            amount_box = form.cleaned_data.get('amount_box')
            popolneni_boxdream(author, amount_box)
            return redirect('operation_ok')


        return render(request, 'boxdream.html', {'form': form,
                                                 'boxdream': boxdream,
                                                 'boxdream_profiles': boxdream_profiles,
                                                 'Leftbeforethedraw': Leftbeforethedraw,
                                                 'need_count_active_dream': need_count_active_dream,
                                                 'flag_dream': flag_dream})


class HistoryDrawBoxVIew(View):

    def get(self, request):

        dreams = HistoryBoxDream.objects.prefetch_related('win_dream').all()

        return render(request, 'history_win_dreams.html', {'dreams': dreams})


class MessagesGood(View):

    def get(self, request):

        return render(request, 'messages_good.html', {})


class OperationOk(View):

    def get(self, request):

        return render(request, 'operation_ok.html', {})


class OperationErrors(View):

    def get(self, request):

        return render(request, 'operations_errors.html', {})



# Модифицированные представления на восстановления пароля -) ==============================

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form_new.html'
    form_class = CustomPasswordResetForm


class CustomePasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done_new.html'


class CustomePasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm_new.html'
    form_class = CustomePasswordResetConfirmForm


class CustomePasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete_new.html'


# ================================================================================