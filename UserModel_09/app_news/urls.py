from django.urls import path
from .views import UserFormView, NewsListView, UserEditFormView, Created_news, EditNews, NewsDetailView, CreadetComment
from .import views


urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('created_news/', Created_news.as_view()),
    path('created_news/<int:profile_id>/edit/', EditNews.as_view(), name='edit-news'),
    path('profiles/registr/', UserFormView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view()),
    path('created_comments/<int:pk>/', CreadetComment.as_view(), name='created-comment')
]
