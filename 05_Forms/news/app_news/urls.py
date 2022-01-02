from django.urls import path
from .views import UserFormView, Index, UserEditFormView, Created_news, EditNews, NewsDetailView
from .import views


urlpatterns = [
    path('', Index.as_view(), name='news-list'),
    path('news_<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('created_news/', Created_news.as_view()),
    path('created_news/<int:profile_id>/edit/', EditNews.as_view()),
    path('profiles/registr/', UserFormView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view()),
]
