from django.urls import path
from .views import RegistrationView, login_view, AnotherLogoutView, Index



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', AnotherLogoutView.as_view(), name='logout'),
    path('', Index.as_view(), name='index'),
]