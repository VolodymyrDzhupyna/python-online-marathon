from django.shortcuts import render
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.response import Response

from library.permissions import IsLibrarianOrAdmin


class AuthorView(viewsets.ModelViewSet):
	queryset=Author.objects.all()
	serializer_class = AuthorSerializer
	permission_classes = [IsLibrarianOrAdmin, ]

	def destroy(self, request, *args, **kwargs):
		author = self.get_object()
		if not author.books.all():
			author.delete()
			return Response({"message": "Author was successfully deleted!"})
		else:
			return Response({"message": "You can`t delete this author, because he`s assigned to one or more books!"})