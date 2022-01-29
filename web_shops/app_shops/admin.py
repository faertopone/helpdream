from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Profile, ProfilePhotos



class PhotoProfileAdmin(admin.ModelAdmin):
    list_display = ['photo', 'id', 'photo_img']

admin.site.register(ProfilePhotos, PhotoProfileAdmin)


class PhotoProfileInLine(admin.StackedInline):
    model = ProfilePhotos
    fields = ('photo', 'photo_img')


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'gender', 'creadet_at', 'id']
    list_filter = ['user', 'creadet_at', 'gender', 'id']
    search_fields = ['user', 'gender', 'id']
    fields = ['user', 'gender']
    inlines = [PhotoProfileInLine]


admin.site.register(Profile, ProfileAdmin)


