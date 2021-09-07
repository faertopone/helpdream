from django.urls import path
from .import views


urlpatterns = [
                 path('advertisement/', views.advertisement_list, name='advertisement_list'),
                 path('', views.index, name='index'),
                 path('kurs_1_list/', views.kurs_1, name='kurs_1_list'),
                 path('kurs_2/', views.kurs_2, name='kurs_2'),
                 path('kurs_3/', views.kurs_3, name='kurs_3'),
                 path('kurs_4/', views.kurs_4, name='kurs_4'),
                 path('kurs_5/', views.kurs_5, name='kurs_5')
            ]