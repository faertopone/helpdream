import datetime

from django.utils.translation import gettext as _
from django.utils.formats import date_format
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.core.cache import cache
from .forms import MyUserRegister
from .forms import LoginForm
from .models import Profile, ProfilePhotos, Shops, PurchaseHistory, Promotions, Stock





def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class Index(View):

    def get(self, request):
        form = LoginForm()
        base_link = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        user_y = request.user
        avatar_x = False
        #Елси пользователь авторизирова и это не админ, то
        if user_y.is_authenticated and user_y.username != 'admin':
            prof_user = Profile.objects.get(user_id=user_y.id)
            avatar = ProfilePhotos.objects.get(id=prof_user.id)
            link = avatar.photo_img
            if link:
                avatar_x = base_link + str(link)


        context = {
            'form': form,
            'avatar': avatar_x
        }

        return render(request, 'index.html', context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                return HttpResponseRedirect(reverse('account_not_active'))
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, 'index.html', context=context)

class RegisterUser(View):

    def get(self, request):
        form = MyUserRegister()
        context = {
            'form': form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        form = MyUserRegister(request.POST, request.FILES)
        if form.is_valid():
            #СОхраним данные юзера
            user = form.save()
            gender = form.cleaned_data.get('gender')
            phone = form.cleaned_data.get('phone')
            #тут сохраним дополнительные параметры юзера
            profile_user = Profile.objects.create(
                user=user,
                gender=gender,
                phone=phone
            )
            profile_user.save()
            avatar = form.cleaned_data.get('avatar')
            #тут сохраним аватар профиля
            ProfilePhotos.objects.create(photo=profile_user, photo_img=avatar)
            #далее сразу залогинимся
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        form = MyUserRegister()
        context = {
            'form': form
        }
        return render(request, 'register.html', context=context)


class ProfileInfo(View):

    def get(self, request):

        #Если пользователь не авторизован - нехер делать в личном кабинете ему
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        user_y = request.user
        # Если админ, пусть идет в свой профиль)
        if user_y.is_superuser:
            return HttpResponseRedirect('/admin')

        #Загружаем информацию этого пользователя
        user_info = User.objects.get(id=request.user.id)

        base_link = 'http://127.0.0.1:8000/ALL_DATA_FILES/'

        history = None

        #ищем обьекты Профиля этого пользователя
        prof_user = Profile.objects.get(user_id=user_y.id)
        #Теперь ищем аватарки этого пользователя
        avatar = ProfilePhotos.objects.get(id=prof_user.id)
        link = avatar.photo_img
        if link:
            avatar_x = base_link + str(link)
        else:
            avatar_x = False
        #Тут ищем обьекты истории этого Профиля
        history = PurchaseHistory.objects.filter(user_history=prof_user)

        #Кеширование только этого
        # promotions = Promotions.objects.all()
        # promotions_cache_key = 'promotions: {}'.format(user_y.username)
        # cache.get_or_set(promotions_cache_key, promotions, 60*60*24)

        #Массово кеширование
        promotions_cache_key = 'promotions: {}'.format(user_y.id)
        offers_cahe_key = 'offers:{}'.format(user_y.id)

        promotions = Promotions.objects.all()
        stock = Stock.objects.all()

        user_account_cache_data = {
            promotions_cache_key: promotions,
            offers_cahe_key: stock
        }

        cache.set_many(user_account_cache_data)



        context = {
            'user': user_info,
            'avatar': avatar_x,
            'history': history,
            'promotions': promotions,
            'stock': stock,
        }

        return render(request, 'profile_user.html', context=context)

class ShopsView(View):

    def get(self, request):
        shops = Shops.objects.all()
        return render(request, 'shops_list.html', {'shops': shops})