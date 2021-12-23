from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_index, name='advertisement_index'),

]