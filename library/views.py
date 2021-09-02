from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from library.serializers import AuthorSerializer, BookSerializer
from library.models import Author, Book
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.status import HTTP_201_CREATED

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        data = request.data

        try:
            name = data.get("name", None)
        except ValueError as value_error:
            raise value_error

        if name:
            if name[0].isdigit():
                raise ValidationError(detail="Author name cannot start with an integer.")
            author = Author(name=name)
            author.save()
            return Response(data=AuthorSerializer(author, many=False).data, status=HTTP_201_CREATED)
        else:
            raise ValidationError(detail="Author name cannot be empty")