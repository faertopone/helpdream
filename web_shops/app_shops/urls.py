from django.contrib.auth import logout
from django.urls import path

from .views import Index, RegisterUser, logout_view

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_view, name='logout')
]