import requests
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import UserForm, LogginForm, CommentsForm, FilterForm
from .forms import MyNewsForm, StandartUser
from .models import My_User, MyNews, MyComments
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, HttpResponseRedirect



class UserFormView(View):

    def get(self, request):
        user_form = StandartUser()
        return render(request, 'users_htmls/User_registration.html', context={'user_form': user_form})

    def post(self, request):
        user_form = StandartUser(request.POST)
        if user_form.is_valid():
            username, email, password1 = (
                user_form.cleaned_data['username'],
                user_form.cleaned_data['email'],
                user_form.cleaned_data['password1'],
            )
            user = User.objects.create_user(username, email, password=password1)
            user.save()
            #А тут сразу его авторизируем, прологинем и перенаправим на главную страницу)
            user = authenticate(username=username, password=password1)
            login(request, user)
            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        errors = user_form.errors

        return render(request, 'users_htmls/User_registration.html', {'errors': errors, 'user_form': user_form})



class NewsListView(View):

    def get(self, request):
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False

        search = FilterForm()

        items_news = MyNews.objects.all()
        return render(request, 'news_htmls/news_list.html', context={'items_news': items_news, 'flagmoder': flagmoder, 'search': search})

    def post(self, request):
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False

        #тут получил переменные с формы фильтра
        search = FilterForm(request.POST)
        #Проверим валидностьи получим значение
        if search.is_valid():
            teg = search.cleaned_data.get('teg')
            data_order = search.cleaned_data.get('data_order')
            #сортировка по возрастанию если True
            if data_order == 'True':
                items_news = MyNews.objects.order_by('created_news')
            else:
                items_news = MyNews.objects.order_by('-created_news')

            filter_items_news = []
            #Тут фильтрует по тэгу
            if not teg == 'all':
                for i in items_news:
                    if teg == i.teg:
                        filter_items_news.append(i)
                        #сортировку перевернем
                        # filter_items_news.reverse()
            else:
                #это выбрано all то создает сюда все обьекты
                for i in items_news:
                    filter_items_news.append(i)

            return render(request, 'news_htmls/news_list.html',
                      context={'items_news': filter_items_news, 'flagmoder': flagmoder, 'search': search})


# class NewsDetailView(DetailView):
#
#     model = MyNews
#     template_name = 'news_htmls/news_detail.html'
#     context_object_name = 'detail_items'

class NewsDetailView(View):

    def get(self, request, pk):
        news = MyNews.objects.get(id=pk)
        coments = MyComments.objects.all()
        coments_list_anonim = []
        coments_list_auth = []
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False


        #тут я взял все коментарии,и у кого Ид совпало с ид новости записываю в массив
        for i in coments:
            if i.id_news_current == pk:
                lfg_name = i.name.split()
                if '(Аноним)' in lfg_name:
                    coments_list_anonim.append(i)
                else:
                    coments_list_auth.append(i)


        return render(request, 'news_htmls/news_detail.html',
                      context={'news': news, 'pk': pk, 'coments_list_anonim': coments_list_anonim, 'coments_list_auth': coments_list_auth, 'flagmoder': flagmoder})


    def post(self, request, pk):
        pass



class EditNews(View):

    def get(self, request, profile_id):
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
            display = 'display: none'
        else:
            flagmoder = False
            display = 'display: block'
        news = MyNews.objects.get(id=profile_id)
        news_form = MyNewsForm(instance=news)

        return render(request, 'news_htmls/edit_news.html',
                      context={'news_form': news_form, 'profile_id': profile_id, 'flagmoder': flagmoder, 'news': news, 'display': display})

    def post(self, request, profile_id):
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False
        news = MyNews.objects.get(id=profile_id)
        news_form = MyNewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return HttpResponseRedirect('/')
        print(news_form)
        return render(request, 'news_htmls/edit_news.html',
                      context={'news_form': news_form, 'profile_id': profile_id, 'flagmoder': flagmoder, 'news': news})


class UserEditFormView(View):

    def get(self, request, profile_id):
        user = My_User.objects.get(id=profile_id)
        user_form = UserForm(instance=user)
        return render(request, 'users_htmls/edit_profil.html', context={'user_form': user_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        user = My_User.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.save()
            return HttpResponseRedirect('/')
        return render(request, 'users_htmls/edit_profil.html', context={'user_form': user_form, 'profile_id': profile_id})


class Created_news(View):

    def get(self, request):
        my_news = MyNewsForm()
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False
        return render(request, 'news_htmls/created_news.html', context={'my_news': my_news, 'flagmoder': flagmoder})

    def post(self, request):
        if request.user.has_perm('app_users.moderator_time'):
            flagmoder = True
        else:
            flagmoder = False

        news_form = MyNewsForm(request.POST)
        my_news = MyNewsForm()
        user_y = request.user
        user_x = User.objects.get(id=user_y.id)
        print(news_form.errors)
        if news_form.is_valid():
            MyNews.objects.create(**news_form.cleaned_data)
            count_x = user_x.profile.count_news
            count_x = +1
            user_x.profile.count_news = count_x
            user_x.profile.save()
            print(news_form.is_valid(), 'news_form.is_valid()')
            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        return render(request, 'news_htmls/created_news.html', context={'my_news': my_news, 'flagmoder': flagmoder})






class CreadetComment(View):

    def get(self, request, pk):
        my_comment = CommentsForm()
        news = MyNews.objects.get(id=pk)
        return render(request, 'news_htmls/created_comment.html', context={'my_comment': my_comment, 'news': news})

    def post(self, request, pk):
        comment_form = CommentsForm(request.POST)

        news = MyNews.objects.get(id=pk)


        if comment_form.is_valid():
            temp = MyComments.objects.create(**comment_form.cleaned_data)
            #Тут мы присвоим ключ по названию новости к этому коментарию)
            if request.user.is_authenticated:
                comment_form.name = request.user.username
            else:
                temp.name = temp.name + ' (Аноним)'
            temp.id_news_current = news.id
            temp.comment = news
            temp.save()
            return HttpResponseRedirect('/')

        print('Не прошло валидность формы')
        errors = comment_form.errors
        my_comment = CommentsForm()
        news = MyNews.objects.get(id=pk)
        return render(request, 'news_htmls/created_comment.html', context={'news': news, 'my_comment': my_comment, 'errors': errors})






