from attr import fields
from rest_framework import serializers
from publication.models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Author
        fields="__all__"

class BookSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Book
        fields="__all__"
