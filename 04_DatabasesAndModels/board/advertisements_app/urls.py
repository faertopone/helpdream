from django.urls import path
from .import views
from .views import AdvertisementListView

urlpatterns = [
    path('', views.advertisement_index, name='advertisement_index'),
    path('advertisements/', AdvertisementListView.as_view(), name='advertisements-list')
]