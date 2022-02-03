from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView

from .forms import LoginForm, MyUserRegister, BuyItems
from .models import Profile, Item


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
                    return HttpResponseRedirect(reverse('index'))

        form = LoginForm()
        return render(request, 'login.html', {'from': form})


class MainIndex(View):
    """
    Представление главной страницы.
    """
    def get(self, request):




        return render(request, 'index.html', {})



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
            Profile.objects.create(
                user=user,
                gender=gender,
                avatar=avatar,
                phone=phone
            )
            #получим данные логин и пароль валидные
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #Залогинимся сразу после регистрации
            user = authenticate(username=username, password=raw_password)
            login(request, user)
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
    queryset = Item.objects.all()


class ItemListDetail(View):

    def get(self, request, pk):

        detail_items = Item.objects.get(pk=pk)

        return render(request, 'items_list_detail.html', {'detail_items': detail_items})

    def post(self, request, pk):
        buy_form = BuyItems(request.POST)
        if buy_form.is_valid():
            id_item = buy_form.cleaned_data.get('id_item')
            count_item = buy_form.cleaned_data.get('count_item')

            #найдем наш товар
            item = Item.objects.get(id=id_item)

            #Так же найдем профиль нашего пользователя
            profile_user = Profile.objects.get(user_id=request.user.id)

