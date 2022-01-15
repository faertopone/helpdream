from django.contrib import admin

# Register your models here.
from .models import Vacancy, Summary


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Vacancy, VacancyAdmin)


class SummaryAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


admin.site.register(Summary, SummaryAdmin)