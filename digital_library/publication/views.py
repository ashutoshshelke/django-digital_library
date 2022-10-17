from django.shortcuts import render
from rest_framework import viewsets
from publication.models import Author,Book
from publication.serializers import AuthorSerializer, BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AuthorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

    #authors/{author_id}/books
    @action(detail=True,methods=['get'])
    def books(self,request,pk=None):
        
        author = Author.objects.get(pk=pk)
        bks = Book.objects.filter(author=author)
        bks_serializer = BookSerializer(bks,many=True,context={'request':request})
        return Response(bks_serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset=Book.objects.all()
    serializer_class=BookSerializer