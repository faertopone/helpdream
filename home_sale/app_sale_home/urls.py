from django.urls import path

from .views import Index_Main, SaleHousListView, ContactsView, AboutView, NewsDetailView
from .feeds import LatestNewsFeed

urlpatterns = [
    path('', Index_Main.as_view(), name='index'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail'),
    path('hous_list/', SaleHousListView.as_view(), name='hous_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about/', AboutView.as_view(), name='about'),
    path('rss/', LatestNewsFeed(), name='rss')
]