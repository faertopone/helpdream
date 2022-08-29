from django.contrib.auth import logout
from django.urls import path

from .views import Index, RegisterUser, logout_view, ProfileInfo, ShopsView
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_view, name='logout'),
    path('profile', ProfileInfo.as_view(), name='profile'),
    path('shops', cache_page(60*60*24*5)(ShopsView.as_view()), name='shops_list'),

]