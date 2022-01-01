from django.urls import path
from .views import UserFormView, Index, UserEditFormView, Created_news
from .import views


urlpatterns = [
    path('', Index.as_view()),
    path('created_news/', Created_news.as_view()),
    path('profiles/registr/', UserFormView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view()),
]
