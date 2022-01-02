from django.shortcuts import render
from django.views import View
from .forms import UserForm, LogginForm
from .forms import MyNewsForm
from .models import User, MyNews
from datetime import datetime
from django.http import HttpResponseRedirect


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'users_htmls/User_registration.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        return render(request, 'users_htmls/User_registration.html', {})



class Index(View):

    def get(self, request):
        news = MyNews.objects.all()
        return render(request, 'news_htmls/index.html', {'news': news})

    def post(self, request):
        loggin = LogginForm()
        if loggin.is_valid():
            return HttpResponseRedirect('/')
        return render(request, 'news_htmls/index.html', {})


class UserEditFormView(View):

    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(instance=user)
        return render(request, 'users_htmls/edit_profil.html', context={'user_form': user_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.save()
        return render(request, 'users_htmls/edit_profil.html', context={'user_form': user_form, 'profile_id': profile_id})


class Created_news(View):

    def get(self, request):
        my_news = MyNewsForm()
        return render(request, 'news_htmls/created_news.html', context={'my_news': my_news})

    def post(self, request):
        news_form = MyNewsForm(request.POST)
        my_news = MyNewsForm()
        if news_form.is_valid():
            MyNews.objects.create(**news_form.cleaned_data)
            print('Новость должна записаться в БД')
            print(news_form.is_valid(), 'news_form.is_valid()')
            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        return render(request, 'news_htmls/created_news.html', context={'my_news': my_news})







    # def get(self, request):
    #     news = NewsForm()
    #     return render(request, 'news_htmls/created_news.html', context={'news': news})
    #
    # def post(self, request, profile_id):
    #     news = News.objects.get(id=profile_id)
    #     news_form = UserForm(request.POST, instance=news)
    #     if news_form.is_valid():
    #         news.save()
    #     return render(request, 'news_htmls/edit_news.html',
    #                   context={'news_form': news_form, 'profile_id': profile_id})