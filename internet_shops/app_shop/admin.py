from django.contrib import admin

from .models import Item, Shops


class ItemAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'price']
    fields = ['name', 'description', 'price', 'amount_item', 'category_item', 'shops']


class ShopsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name', 'adress', 'tel']


admin.site.register(Item, ItemAdmin)
admin.site.register(Shops, ShopsAdmin)