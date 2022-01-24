import os
from _csv import reader
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

from .forms import AuthForm, MyUserRegister, EditFormUser, BlogForm, UploadFileCsv
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
            avatar = reg_form.cleaned_data.get('avatar')
            Profile.objects.create(
                user=user,
                phone=phone,
                avatar=avatar

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
        if user_curent.username != 'admin':
            avatar_link = temp + str(user_curent.profile.avatar)
        else:
            avatar_link = ''
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
        blog_form = BlogForm()

        return render(request, 'blog/created_blog.html', {'blog_form': blog_form})

    def post(self, request):
        blog_form = BlogForm(request.POST, request.FILES)

        dt = datetime.now()
        dt_now = dt.strftime("%d%m%y-%H-%M-%S")
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/img_blog/'
        if blog_form.is_valid():
            blog_id = blog_form.cleaned_data.get('id')
            title = blog_form.cleaned_data.get('title')
            description = blog_form.cleaned_data.get('description')
            author = request.user.username
            links_str_img = ''
            links_img = []
            files_multi_img = request.FILES.getlist('multi_img')
            for f_img in files_multi_img:
                links_img.append(temp + str(f_img))
                Blog(file_img=f_img)
                print('Сохарнение файла')
            for i in links_img:
                links_str_img += i + ' '

            Blog.objects.create(id=blog_id, title=title, description=description, author=author, multi_link_file_img=str(links_str_img))


            return HttpResponseRedirect('/')



        return render(request, 'blog/created_blog.html', {'blog_form': blog_form})

class UploadAllBlog(View):
    def get(self, request):
        file_csv_form = UploadFileCsv()
        return render(request, 'blog/upload_file_blog.html', {'file_csv_form': file_csv_form})

    def post(self, request):
        file_form = UploadFileCsv(request.POST, request.FILES)
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)
        if file_form.is_valid():
            try:
                blog_file = file_form.cleaned_data.get('file_csv').read()
                blog_str = blog_file.decode('utf-8').split('\n')
                csv_reader = reader(blog_str, delimiter=",", quotechar='"')
                author = user_curent.username
                title = 'Блог загружен через csv'

                for row in csv_reader:
                    if len(row) != 0:
                        row_z = row[1]
                        data_time_str = datetime.strptime(row_z, "%d/%m/%y %H:%M:%S")
                        temp = Blog.objects.create(author=author, description=row[0], title=title)
                        temp.creadet_at = data_time_str
                        temp.save()
            except Exception as error:
                file_csv_form = UploadFileCsv()
                return render(request, 'blog/upload_file_blog.html', {'file_csv_form': file_csv_form, 'error': error})
            return HttpResponseRedirect('/')

        file_csv_form = UploadFileCsv()
        return render(request, 'blog/upload_file_blog.html', {'file_csv_form': file_csv_form})