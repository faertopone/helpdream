import os
import time
from _csv import reader
from datetime import datetime

from django.core.mail import send_mail
from django.forms.utils import ErrorList
from django.contrib import messages
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import DetailView

from .forms import AuthForm, MyUserRegister, EditFormUser, BlogForm, UploadFileCsv, BlogPhotoForm, RestorePasswordForm
from .models import Profile, Blog, BlogPhoto


class Login_view(View):

    def post(self, request):
        auth_form = AuthForm(request.POST)
        my_errors = ''
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
                my_errors = 'Ошибка!\n Проверьте правильность логина и пароля'
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность логина и пароля')

        return render(request, 'users/login.html', {'form': auth_form, 'my_errors': my_errors})





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
        admin_user = request.user.username
        flag_admin = False
        if admin_user == 'admin':
            flag_admin = True

        return render(request, 'blog/index.html', {'blog_list': blog, 'flag_admin': flag_admin})

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
        if user_curent.username != 'admin' and (user_curent.profile.avatar != ''):
            avatar_link = temp + str(user_curent.profile.avatar)
        else:
            avatar_link = False
        return render(request, 'Users/profile_user.html', {'user_curent': user_curent, 'avatar_link': avatar_link})

    def post(self, requset):
        pass

class Profile_user_edit(View):

    def get(self, request):
        reg_form = EditFormUser()
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)
        # Я вот так сделал путь, но мне кажеться он должен как то подругому делаться?)))
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        if user_curent.username != 'admin':
            avatar_link = temp + str(user_curent.profile.avatar)
        else:
            avatar_link = ''

        return render(request, 'Users/profil_user_edit.html', {'reg_form': reg_form, 'user_curent': user_curent, 'avatar_link': avatar_link})

    def post(self, request):
        reg_form = EditFormUser(request.POST, request.FILES)
        user_y = request.user
        user_curent = User.objects.get(id=user_y.id)
        # Я вот так сделал путь, но мне кажеться он должен как то подругому делаться?)))
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        if user_curent.username != 'admin':
            avatar_link = temp + str(user_curent.profile.avatar)
        else:
            avatar_link = ''
        if reg_form.is_valid():
            name = reg_form.cleaned_data.get('name')
            last_name = reg_form.cleaned_data.get('last_name')
            user_curent.first_name = name
            user_curent.last_name = last_name
            user_curent.save()
            return HttpResponseRedirect('/profile_info/')

        reg_form = MyUserRegister(request.POST)

        return render(request, 'Users/profil_user_edit.html', {'reg_form': reg_form, 'errors': reg_form.errors, 'avatar_link': avatar_link})


class Blog_full_info(View):

    def get(self, request, blog_id):
        blog_items = Blog.objects.get(id=blog_id)
        links = blog_items.multi_link_file_img
        links_img = links.split()
        img_link = []
        blog_photo = BlogPhoto.objects.all()
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/'
        for i in blog_photo:
            if i.blog_id == blog_items.id:
                img_link.append(temp + str(i.file_img))

        print(img_link)

        return render(request, 'blog/blog_full_info.html', {'blog_items': blog_items, 'blog_id': blog_id, 'links_img': links_img, 'img_link': img_link})



class CreatedBlog(View):

    def get(self, request):
        blog_form = BlogForm()
        blog_photo_form = BlogPhotoForm()
        return render(request, 'blog/created_blog.html', {'blog_form': blog_form, 'blog_photo_form': blog_photo_form})

    def post(self, request):
        blog_form = BlogForm(request.POST)
        blog_photo_form = BlogPhotoForm(request.FILES)
        dt = datetime.now()
        dt_now = dt.strftime("%d%m%y-%H-%M-%S")
        temp = 'http://127.0.0.1:8000/ALL_DATA_FILES/img_blog/'
        if blog_form.is_valid() and blog_photo_form.is_valid():
            title = blog_form.cleaned_data.get('title')
            description = blog_form.cleaned_data.get('description')
            author = request.user.username
            links_str_img = ''
            links_img = []
            files_multi_img = request.FILES.getlist('multi_img')

            for f_img in files_multi_img:
                links_img.append(temp + str(f_img))

            for i in links_img:
                links_str_img += i + ' '


            temp = Blog.objects.create(title=title, description=description, author=author, multi_link_file_img=str(links_str_img))

            for f_img in files_multi_img:
                BlogPhoto(file_img=f_img, blog=temp).save()

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



class RestorePassword(View):

    def get(self, request):
        restore_form = RestorePasswordForm()
        return render(request, 'Users/restore_password.html', {'form': restore_form})

    def post(self, request):
        restore_form = RestorePasswordForm(request.POST)
        if restore_form.is_valid():
            send_mail(
                subject='Восстановление пароля',
                message='Тут текст с сообщением',
                from_email='admin@mail.ru',
                recipient_list=['any@mail.ru']
            )
            return HttpResponseRedirect('/succes')

        return render(request, 'Users/restore_password.html', {'form': restore_form})


def succes(request):
    return render(request, 'complete/succes.html')

