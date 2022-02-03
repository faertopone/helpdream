from django.urls import path
from .views import MainIndex, ItemList, ItemListDetail, MyLogoutView, LoginView, Register

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('itemslist/', ItemList.as_view(), name='items_list'),
    path('itemslist/<int:pk>', ItemListDetail.as_view(), name='items_list-detail'),
]