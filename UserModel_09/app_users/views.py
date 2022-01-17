
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import AuthForm, ExtendedREgisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class profile_data_view(View):

    def get(self, request):
        profile_user = request.user
        form = ExtendedREgisterForm(instance=profile_user)
        return render(request, 'users/profile.html', {'profile_user': profile_user})



class profile_edit_view(View):

    def get(self, request):
        profile_user = request.user
        # form_list - тут выведем форму для текущего пользователя
        form_list = ExtendedREgisterForm(instance=profile_user)
        return render(request, 'users/profile_edit.html', {'form_list': form_list})

    def post(self, request):
        profile_user = request.user
        #Это form - принимаем аднные после заполенния и првоерим валидность
        form = ExtendedREgisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                phone=phone,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

