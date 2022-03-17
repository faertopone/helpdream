from django.contrib import admin
from .models import Profile,  WriteDeam, WhoHelpMe
from django.utils.translation import gettext_lazy as _

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'age', 'my_balance']


class WriteDeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'who_dream', 'id', 'mini_description']

    # Это название когда в админке выбираем Актион чойсе
    actions = ['dream_is_active', 'dream_is_no_active', 'dream_is_complete_on', 'dream_is_complete_off']


    def dream_is_active(self, request, queryset):
        queryset.update(dream_is_active=True)


    def dream_is_no_active(self, request, queryset):
        queryset.update(dream_is_active=False)

    def dream_is_complete_on(self, request, queryset):
        queryset.update(dream_is_complete=True)

    def dream_is_complete_off(self, request, queryset):
        queryset.update(dream_is_complete=False)


    dream_is_active.short_description = _('мечта-активна')
    dream_is_no_active.short_description = _('мечта-не активна')
    dream_is_complete_on.short_description = _('завершить мечту')
    dream_is_complete_off.short_description = _('отменить завершение мечту')


class WhoHelpMeAdmin(admin.ModelAdmin):

    list_display = ['id', 'who_price', 'help_profile']






admin.site.register(WhoHelpMe, WhoHelpMeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(WriteDeam, WriteDeamAdmin)


