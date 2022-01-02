from django.contrib import admin
from .models import User, MyNews, MyComments


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(MyNews)
class MyNewsAdmin(admin.ModelAdmin):
    pass


@admin.register(MyComments)
class MyCommentsAdmin(admin.ModelAdmin):
    pass