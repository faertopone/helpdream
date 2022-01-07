from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView



def login_view(request):
    if request.method == 'POST':  # для POST пытаемся аутенфицировать пользователя
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


    else:  # для всех остальных запросов отображаем страничку логина
        auth_form = AuthForm()

    context = {
            'form': auth_form
            }
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли')

class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html' или сюда
    next_page = '/'  # или перенаправление сюда