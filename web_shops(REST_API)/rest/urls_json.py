from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='json_items'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='items_detail')
]