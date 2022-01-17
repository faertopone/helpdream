from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'date_of_birth', 'phone', 'count_news']
    list_filter = ['city', 'phone', 'user']
    search_fields = ['user', 'phone']
    fields = ('user', 'city', 'date_of_birth', 'phone', 'count_news', 'flag_veryfication')


admin.site.register(Profile, ProfileAdmin)