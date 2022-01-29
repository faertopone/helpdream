from django.utils.translation import gettext as _
from django.utils.formats import date_format
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User

from .forms import MyUserRegister
from .forms import LoginForm
from .models import Profile, ProfilePhotos


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class Index(View):

    def get(self, request):
        form = LoginForm()
        base_link = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        user_y = request.user
        if user_y.is_authenticated and user_y.username != 'admin':
            prof_user = Profile.objects.get(user_id=user_y.id)
            avatar = ProfilePhotos.objects.get(id=prof_user.id)
            link = avatar.photo_img
            avatar_x = base_link + str(link)

        else:
            avatar_x = False

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
            #тут сохраним дополнительные параметры юзера
            provile_user = Profile.objects.create(
                user=user,
                gender=gender
            )
            provile_user.save()
            avatar = form.cleaned_data.get('avatar')
            #тут сохраним аватар профиля
            ProfilePhotos.objects.create(photo=provile_user, photo_img=avatar)
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