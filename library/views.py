from library.serializers import BookSerializer
from library.models import Book
from django.shortcuts import render
from rest_framework import viewsets, permissions

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]