from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
# Create your views here.
from .models import Vacancy, Summary


def vacancy_list(request):
    # Это если без декоратора
    # Проверка прав пользователя
    if not request.user.has_perm('app_employment.publish'):  #<app>.<action>_<object_name>
        return HttpResponse('У Вас нету прав на это!')
        # return HttpResponseRedirect('/')
    current_user = request.user
    vacancies = Vacancy.objects.all()
    rezume_list = Summary.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies, 'rezume_list': rezume_list, 'current_user': current_user})

