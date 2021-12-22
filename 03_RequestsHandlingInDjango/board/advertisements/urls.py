from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('about/', views.about_list, name='about_list'),
    path('regions/', views.Region.as_view()),
]
