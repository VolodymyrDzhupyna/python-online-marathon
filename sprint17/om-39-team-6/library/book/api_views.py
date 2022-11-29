from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

from library.permissions import IsLibrarianOrAdminOrReadOnly


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrAdminOrReadOnly, ]