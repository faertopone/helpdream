from django.urls import path
from django.contrib.auth import views
from django.views.decorators.cache import cache_page
from .views import IndexView, LoginView, RegisterView, UserLkView, RestorePasswordView, logout_view, WriteDreamView, \
    OtherDreamView, \
    DetailDreamView, CompleteDreamsView, TOPHumansView, EditProfile, AboutView, BoxDreamView, HistoryDrawBoxVIew, \
    MessagesGood, OperationOk, OperationErrors, CustomPasswordResetView, CustomePasswordResetDoneView, CustomePasswordResetConfirmView,CustomePasswordResetCompleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_lk/', UserLkView.as_view(), name='user_lk'),
    path('user_lk/edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path('restore_password/', RestorePasswordView.as_view(), name='restore_password'),
    path('writedream/', WriteDreamView.as_view(), name='writedream'),
    path('otherdream/', OtherDreamView.as_view(), name='otherdream'),
    path('detaildream/<int:pk>', DetailDreamView.as_view(), name='detail_dream'),
    path('complete_dreams/', CompleteDreamsView.as_view(), name='complete_dreams'),
    path('top/', TOPHumansView.as_view(), name='top'),
    #Кешируем всю страницу в секундах на 5 дней
    path('about/', cache_page(60*60*24*5)(AboutView.as_view()), name='about'),
    path('boxdream/', BoxDreamView.as_view(), name='boxdream'),
    path('historywin/', HistoryDrawBoxVIew.as_view(), name='historywin'),
    path('about/messagesgood', MessagesGood.as_view(), name='messagesgood'),
    path('boxdream/operation_ok', OperationOk.as_view(), name='operation_ok'),
    path('boxdream/operation_errors', OperationErrors.as_view(), name='operation_errors'),

    # restore password urls (Я изменил шаблоны на свои)
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomePasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomePasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomePasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
