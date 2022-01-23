from django.contrib import admin
from .models import Item, File
# Register your models here.


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_item', 'price')

admin.site.register(Item,ItemsAdmin)


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'description' )

admin.site.register(File,FileAdmin)