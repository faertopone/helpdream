from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'date_of_birth']
    list_filter = ['city']
    search_fields = ['user']


admin.site.register(Profile, ProfileAdmin)