from library.models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, required=True, allow_null=False)

    class Meta:
        model = Book
        fields = ['id', 'author', 'isbn', 'price']