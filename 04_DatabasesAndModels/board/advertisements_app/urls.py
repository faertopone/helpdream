from django.urls import path
from .import views
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('', views.advertisement_index, name='advertisement_index'),
    path('advertisements/', AdvertisementListView.as_view(), name='advertisements-list'),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name='advertisements-detail'),
]