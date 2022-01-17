from django.urls import path
from .views import login_view, AnotherLoginView, logout_view, AnotherLogoutView, login_view, register_view, best_register_view, profile_data_view, profile_edit_view
from django.urls import include


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('register/', register_view, name='register'),
    path('best_register/', best_register_view, name='best_register'),
    path('profile/', profile_data_view.as_view(), name='profile_data_view'),
    path('profile_edit/', profile_edit_view.as_view(), name='profile_edit_view'),

]