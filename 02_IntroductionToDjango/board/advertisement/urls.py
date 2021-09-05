from django.urls import path
from .import views


urlpatterns = [
                 path('advertisement/', views.advertisement_list, name='advertisement_list'),
                 path('', views.index_list, name='index_list')
            ]