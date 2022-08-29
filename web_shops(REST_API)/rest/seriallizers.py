from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ItemModel, Book, AuthorBook


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_staff', 'username', 'email']



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ['id', 'name', 'description', 'weight']





#Туту что вывести в РЕСТ АПИ про кинги
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'yearofissue', 'numberofpages', 'author_book']



#Туту что вывести в РЕСТ АПИ про Авторов книги
class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBook
        fields = ['id', 'name', 'lastname', 'yearofbirth']