from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
from .models import Vacancy, Summary


def vacancy_list(request):
    # Это если без декоратора
    # Проверка прав пользователя
    if not request.user.has_perm('app_employment.view_vacancy'):  #<app>.<action>_<object_name>
        return HttpResponseRedirect('/')
    vacancies = Vacancy.objects.all()
    rezume_list = Summary.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies, 'rezume_list': rezume_list})

