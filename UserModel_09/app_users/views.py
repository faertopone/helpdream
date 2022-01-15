
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import AuthForm, ExtendedREgisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



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

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form} )

def best_register_view(request):
    if request.method == 'POST':
        form = ExtendedREgisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth

            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedREgisterForm()
    return render(request, 'users/register.html', {'form': form} )