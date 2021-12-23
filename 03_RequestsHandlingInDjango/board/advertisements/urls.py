from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view()),
    path('сontacts/', views.Contacts.as_view()),
    path('regions/', views.Region.as_view()),
    path('advertisements/', views.Advertisements.as_view())
]
