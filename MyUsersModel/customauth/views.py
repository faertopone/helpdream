from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from .admin import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.views import View
from django.contrib.auth.models import User
from .forms import AuthForm



def login_view(request):
    if request.method == 'POST':  # для POST пытаемся аутенфицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            email = auth_form.cleaned_data['email']
            password = auth_form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    auth_form.add_error('__all__', 'Ошибка Учетная запись пользователя не активна')

            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность логина и пароля')


    else:  # для всех остальных запросов отображаем страничку логина
        auth_form = AuthForm()

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
        user_form = UserCreationForm()
        return render(request, 'register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            email, date_of_birth, password = (
                user_form.cleaned_data['email'],
                user_form.cleaned_data['date_of_birth'],
                user_form.cleaned_data['password'],

            )
            user = User.objects.create_user(email, date_of_birth, password)
            user.save()

            return HttpResponseRedirect('/')
        print('Не прошло валидность формы')
        errors = user_form.errors

        return render(request, 'register.html', {'errors': errors, 'user_form': user_form})