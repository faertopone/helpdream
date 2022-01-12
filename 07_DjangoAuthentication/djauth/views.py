from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from .admin import UserChangeForm
from django.contrib.auth.views import LogoutView
from django.views import View
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':  # для POST пытаемся аутенфицировать пользователя
        auth_form = UserChangeForm(request.POST)
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


    else:  # для всех остальных запросов отображаем страничку логина
        auth_form = UserChangeForm()

    context = {
            'form': auth_form
            }
    return render(request, 'login.html', context=context)



class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html' или сюда
    next_page = '/'  # или перенаправление сюда

class Index(View):
    def get(self, request):

        return render(request, 'index.html', {})

class RegistrationView(View):

    def get(self, request):
        user_form = UserChangeForm()
        return render(request, 'register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserChangeForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(**user_form.cleaned_data)
            user.save()
            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        errors = user_form.errors

        return render(request, 'register.html', {'errors': errors, 'user_form': user_form})