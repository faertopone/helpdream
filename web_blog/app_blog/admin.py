from django.contrib import admin
from .models import Blog, Profile
from django.utils.translation import gettext_lazy as _
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'min_description', 'creadet_at', 'id']
    list_filter = ['title', 'creadet_at']
    search_fields = ['title', 'creadet_at']
    fields = ['author', 'title', 'description']


admin.site.register(Blog, BlogAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    list_filter = ['user', ]
    search_fields = ['user', ]

admin.site.register(Profile, ProfileAdmin)