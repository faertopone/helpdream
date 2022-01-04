from django.contrib import admin
from .models import User, MyNews, MyComments


# Register your models here.

#---------------------------------------------------
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# # Еще можно так добавить в админку
# admin.site.register(User, UserAdmin)
#---------------------------------------------------


class CommentInLine(admin.StackedInline):
    model = MyComments
    fieldsets = (
        ('Имя', {
            'fields': ('name', 'nickname')
        }),
        ('Описание и город', {
            'description': 'Описание через дескриптион',
            'classes': ('collapse',),
            'fields': ('description', 'city')
        })
    )


class MyNewsAdmin(admin.ModelAdmin):
    list_display = ['titlenews', 'id', 'created_news', 'is_active_news']
    list_filter = ['is_active_news']
    search_fields = ['titlenews']
    inlines = [CommentInLine]

    #Это название когда в админке выбираем Актион чойсе
    actions = ['mark_as_active', 'mark_as_deactive']


    #Если выбрали mark_as_active - тогда is_active_news  делаем True
    def mark_as_active(self, request, queryset):
        queryset.update(is_active_news=True)

    # Если выбрали mark_as_deactive - тогда is_active_news  делаем False
    def mark_as_deactive(self, request, queryset):
        queryset.update(is_active_news=False)

    mark_as_active.short_description = 'Перевести в статус АКТИВНО'
    mark_as_deactive.short_description = 'Перевести в статус Не активно'


admin.site.register(MyNews, MyNewsAdmin)


@admin.register(MyComments)
class MyCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'status_comment', 'id', 'created_comments', 'city', 'nickname']
    # fields = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']
    fieldsets = (
        ('Имя и новость которуму этот коментарий', {
            'fields': ('name', 'nickname', 'comment')
        }),
        ('Описание и город', {
            'description': 'Описание через дескриптион',
            'classes': ('collapse',),
            'fields': ('description', 'city')
        })
    )

    # Это название когда в админке выбираем Актион чойсе
    actions = ['delete_comment_admin', 'restore_comment']

    # Если выбрали delete_comment_admin - тогда status_comment  делаем True
    def delete_comment_admin(self, request, queryset):
        queryset.update(status_comment=True)

    # Если выбрали restore_comment - тогда status_comment  делаем False
    def restore_comment(self, request, queryset):
        queryset.update(status_comment=False)

    # Это название когда в админке выбираем Актион чойсе (с русским описанием
    delete_comment_admin.short_description = 'Удалить коммент админом'
    restore_comment.short_description = 'Вернуть удаленный коммент'




