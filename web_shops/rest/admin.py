from django.contrib import admin

from .models import ItemModel


class ItemsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'weight']

admin.site.register(ItemModel, ItemsModelAdmin)