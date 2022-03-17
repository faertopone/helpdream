from django.contrib import admin

from .models import Post, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)