from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from requests import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .enities import Item
from .seriallizers import ItemSerializer, BookSerializer, AuthorBookSerializer
from .models import ItemModel, AuthorBook, Book
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


# class ItemList(APIView):
#     def get(self, request):
#         items = ItemModel.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


#
#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
#







class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    # queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = ItemModel.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset


    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


#Тут уже выводим обьекты из БД на страницу HTML
class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):

    serializer_class = BookSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        querysetBook = Book.objects.all()
        querysetAuthorBook = AuthorBook.objects.all()

        #Фильтрация по названию книги
        item_name = self.request.query_params.get('name')
        if item_name:
            querysetBook = querysetBook.filter(name=item_name)

        # Фильтрация по названию Автору книги
        item_author_book = self.request.query_params.get('author_book')
        if item_author_book:
            querysetAuthorBook = querysetAuthorBook.filter(name=item_author_book).first()
            querysetBook = Book.objects.filter(author_book=querysetAuthorBook)

        # Выводит результат где введенное число будет типа 10, значит выведет все что больше 10
        count_page = self.request.query_params.get('amount_of_pag__gt')
        if count_page:
            querysetBook = Book.objects.filter(numberofpages__gt=count_page)

        # Выводит результат где введенное число будет типа 10, значит выведет все что больше или равно 10
        count_page = self.request.query_params.get('amount_of_pag__gte')
        if count_page:
            querysetBook = Book.objects.filter(numberofpages__gte=count_page)


        # Выводит результат где введенное число будет типа 10, значит выведет все что меньше 10
        count_page = self.request.query_params.get('amount_of_pag__lt')
        if count_page:
            querysetBook = Book.objects.filter(numberofpages__lt=count_page)


        # Выводит результат где введенное число будет типа 10, значит выведет все что меньше 10 или равно 10
        count_page = self.request.query_params.get('amount_of_pag__lte')
        if count_page:
            querysetBook = Book.objects.filter(numberofpages__lte=count_page)

        # Выводит результат, где введенное число будет = введеному
        count_page = self.request.query_params.get('amount_of_pag')
        if count_page:
            querysetBook = Book.objects.filter(numberofpages=count_page).order_by('name')

        return querysetBook


    def get(self, request):
        return self.list(request)


    def post(self, request, format=None):
        return self.create(request)


class AuthorBookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = AuthorBook.objects.all()
        #фильтрация по имени
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter('name')
        return queryset


    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)