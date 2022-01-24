from django.urls import path
from .views import MainIndex, Login_view, logout_view, RegisterView, ProfileInfo, Profile_user_edit, Blog_full_info, CreatedBlog, UploadAllBlog

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('login/', Login_view.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile_info/', ProfileInfo.as_view(), name='profile_info'),
    path('profile_user_edit/', Profile_user_edit.as_view(), name='profile_user_edit'),
    path('blog_info/<int:blog_id>/', Blog_full_info.as_view(), name='blog_info'),
    path('created_blog/', CreatedBlog.as_view(), name='created_blog'),
    path('upload_file_blog/', UploadAllBlog.as_view(), name='upload_file_blog'),
]