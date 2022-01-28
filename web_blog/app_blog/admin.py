from django.contrib import admin
from .models import Blog, Profile
from django.utils.translation import gettext_lazy as _
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'min_description_admin', 'creadet_at', 'id']
    list_filter = ['title', 'creadet_at']
    search_fields = ['title', 'creadet_at']
    fields = ['author', 'title', 'description']

    #Это сделал для того что бы в админ панели выводилось краткое описание
    def min_description_admin(self, obj):
        text_str = obj.description
        text = list(text_str)
        if len(text) > 15:
            obj.description = text_str[:15] + '...'
        return obj.description

    min_description_admin.short_description = _('Descriptions mini')


admin.site.register(Blog, BlogAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    list_filter = ['user', ]
    search_fields = ['user', ]

admin.site.register(Profile, ProfileAdmin)