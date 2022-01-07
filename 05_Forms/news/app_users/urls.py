from django.urls import path
from .views import login_view, AnotherLoginView, logout_view,AnotherLogoutView
from django.urls import include


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login')
]