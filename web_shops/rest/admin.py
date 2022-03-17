from django.contrib import admin

from .models import ItemModel, AuthorBook, Book


class ItemsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'weight']

admin.site.register(ItemModel, ItemsModelAdmin)



class BookInline(admin.StackedInline):
    model = Book
    list_display = ['name', 'isbn', 'id']
    fields = ('name', 'isbn', 'yearofissue', 'numberofpages', 'author_book')


class AuthorBookAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'yearofbirth']
    fields = ['name', 'lastname', 'yearofbirth']
    inlines = [BookInline]

admin.site.register(AuthorBook, AuthorBookAdmin)












