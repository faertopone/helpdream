from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ItemModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_staff', 'username', 'email']



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ['name', 'description', 'weight']