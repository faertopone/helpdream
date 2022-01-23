import os
from datetime import datetime

import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import DetailView

from .forms import AuthForm, MyUserRegister, EditFormUser, BlogForm,  MultiFormImg
from .models import Profile, Blog


class Login_view(View):

    def post(self, request):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    auth_form.add_error('__all__', 'Ошибка Учетная запись пользователя не активна')

            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность логина и пароля')

        context = {
            'form': auth_form
        }

        return render(request, 'users/login.html', context=context)

    def get(self, request):
        auth_form = AuthForm()
        context = {
                'form': auth_form
                }
        return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class MainIndex(View):
    def get(self, request):
        blog = Blog.objects.all().order_by('-creadet_at')
        return render(request, 'blog/index.html', {'blog_list': blog})

    def post(self, request):
        pass

class RegisterView(View):

    def post(self, request):
        reg_form = MyUserRegister(request.POST, request.FILES)
        if reg_form.is_valid():
            user = reg_form.save()
            phone = reg_form.cleaned_data.get('phone')
            Profile.objects.create(
                user=user,
                phone=phone,

            )
            username = reg_form.cleaned_data.get('username')
            raw_password = reg_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'Users/register.html', {'form': reg_form})

    def get(self, request):
        reg_form = MyUserRegister()
        return render(request, 'Users/register.html', {'form': reg_form})


class ProfileInfo(View):
    def get(self, request):
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)

        #Я вот так сделал путь, но мне кажеться он должен как то подругому делаться?)))
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        avatar_link = temp + str(user_curent.profile.avatar)
        return render(request, 'Users/profile_user.html', {'user_curent': user_curent, 'avatar_link': avatar_link})

    def post(self, requset):
        pass

class Profile_user_edit(View):

    def get(self, request):
        reg_form = EditFormUser()
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)
        return render(request, 'Users/profil_user_edit.html', {'reg_form': reg_form, 'user_curent': user_curent})

    def post(self, request):
        reg_form = EditFormUser(request.POST, request.FILES)
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)
        if reg_form.is_valid():
            name = reg_form.cleaned_data.get('name')
            last_name = reg_form.cleaned_data.get('last_name')
            user_curent.first_name = name
            user_curent.last_name = last_name
            user_curent.save()
            return HttpResponseRedirect('/profile_info/')

        reg_form = MyUserRegister(request.POST)
        print('Не прошло валидность')
        return render(request, 'Users/profil_user_edit.html', {'reg_form': reg_form, 'errors': reg_form.errors})


class Blog_full_info(View):

    def get(self, request, blog_id):
        blog_items = Blog.objects.get(id=blog_id)
        links = blog_items.multi_link_file_img
        links_img = links.split()

        return render(request, 'blog/blog_full_info.html', {'blog_items': blog_items, 'blog_id': blog_id, 'links_img': links_img})



class CreatedBlog(View):

    def get(self, request):
        cur_user = request.user
        blog_form = BlogForm(instance=cur_user)
        multi_form_img = MultiFormImg()
        return render(request, 'blog/created_blog.html', {'blog_form': blog_form, 'multi_form_img': multi_form_img})

    def post(self, request):
        blog_form = BlogForm(request.POST,  request.FILES)
        multi_form_img = MultiFormImg(request.FILES)
        dt = datetime.now()
        dt_now = dt.strftime("%d%m%y-%H-%M-%S")
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/img_blog/'
        if blog_form.is_valid():
            files_img = blog_form.cleaned_data.get('img_field')
            link = temp + str(files_img)
            title = blog_form.cleaned_data.get('title')
            description = blog_form.cleaned_data.get('description')
            author = request.user.username
            IMG = Blog(file_img=files_img)
            IMG.save()

            links_str_img = ''
            if multi_form_img.is_valid():
                print('Мульитформа валидна')
                links_str_img = ''
                links_img = []
                files_multi_img = request.FILES.getlist('multi_img')
                for f_img in files_multi_img:
                    links_img.append(temp + str(f_img))
                    instance = Blog(file_img=f_img)
                    instance.save()

                for i in links_img:
                    links_str_img += i + ' '
            Blog.objects.create(title=title, description=description, author=author, link_file_img=link, multi_link_file_img=str(links_str_img))

            return HttpResponseRedirect('/')



        return render(request, 'blog/created_blog.html', {'blog_form': blog_form, 'multi_form_img': multi_form_img})

