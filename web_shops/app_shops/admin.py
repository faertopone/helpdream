from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Profile, ProfilePhotos, Shops, PurchaseHistory, Promotions, Stock



class PhotoProfileAdmin(admin.ModelAdmin):
    list_display = ['photo', 'id', 'photo_img']

admin.site.register(ProfilePhotos, PhotoProfileAdmin)


class PhotoProfileInLine(admin.StackedInline):
    model = ProfilePhotos
    fields = ('photo', 'photo_img')

class HistoryProfileInLine(admin.StackedInline):
    model = PurchaseHistory
    fields = ('name_product', 'price', 'count_product')


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'gender', 'creadet_at', 'id']
    list_filter = ['user', 'creadet_at', 'gender', 'id']
    search_fields = ['user', 'gender', 'id']
    fields = ['user', 'gender']
    inlines = [PhotoProfileInLine, HistoryProfileInLine]


admin.site.register(Profile, ProfileAdmin)








class ShopsAdmin(admin.ModelAdmin):
    list_display = ['name', 'adress', 'tel', 'id']
    list_filter = ['name', 'adress']
    search_fields = ['name', 'tel', 'adress']

admin.site.register(Shops, ShopsAdmin)



class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',  'active', 'created_at', 'id']
    list_filter = ['name', 'created_at',  'active']
    search_fields = ['name', 'created_at', 'active']

    # Это название когда в админке выбираем Актион чойсе
    actions = ['active', 'deactive']

    # Если выбрали mark_as_active - тогда is_active_news  делаем True
    def active(self, request, queryset):
        queryset.update(active=True)


    # Если выбрали mark_as_deactive - тогда is_active_news  делаем False
    def deactive(self, request, queryset):
        queryset.update(active=False)

    active.short_description = _('Сделать активно')
    deactive.short_description = _('Сделать не активно')


admin.site.register(Promotions, PromotionsAdmin)




class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active', 'created_at', 'id']
    list_filter = ['name', 'created_at',  'active']
    search_fields = ['name', 'created_at',  'active']

    # Это название когда в админке выбираем Актион чойсе
    actions = ['active', 'deactive']

    # Если выбрали mark_as_active - тогда is_active_news  делаем True
    def active(self, request, queryset):
        queryset.update(active=True)

    # Если выбрали mark_as_deactive - тогда is_active_news  делаем False
    def deactive(self, request, queryset):
        queryset.update(active=False)

    active.short_description = _('Сделать активно')
    deactive.short_description = _('Сделать не активно')

admin.site.register(Stock, StockAdmin)