from django.contrib import admin

from .models import News, Housing, TypeHousing, NumberRooms


class NewsAdmin(admin.ModelAdmin):

    list_display = ['title', 'id']

admin.site.register(News, NewsAdmin)


class TypeHousingInline(admin.StackedInline):
    model = TypeHousing
    fields = ['name', 'description']

class NumberRoomsInline(admin.StackedInline):

    model = NumberRooms
    fields = ['rooms_count']




class HousingAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', ]
    inlines = [TypeHousingInline, NumberRoomsInline]

admin.site.register(Housing, HousingAdmin)