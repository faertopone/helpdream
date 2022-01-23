from django.urls import path
from .views import items_list, update_price, Model_form_upload

urlpatterns = [
    path('items/', items_list, name='item_list'),
    path('update_price/', update_price, name='update_price'),
    path('file_upload/', Model_form_upload.as_view(), name='file_upload'),

]