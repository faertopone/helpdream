from django.urls import path, include
from rest_framework import routers
from .api import UserViewSet
from .views import ItemList, BookList, AuthorBookList

router = routers.DefaultRouter()
router.register('users', UserViewSet)

#это если нужно еще добавить путь)
# router.register('users2', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book_List'),
    path('author_books/', AuthorBookList.as_view(), name='author_books')

]

