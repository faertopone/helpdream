from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from requests import Response
from rest_framework.response import Response
from .enities import Item
from .seriallizers import ItemSerializer
from .models import ItemModel
from rest_framework.views import APIView


class ItemList(APIView):
    def get(self, request):
        items = ItemModel.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
