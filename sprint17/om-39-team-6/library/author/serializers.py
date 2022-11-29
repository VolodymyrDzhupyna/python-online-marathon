from rest_framework import serializers
from .models import Author

from book.models import Book

class AuthorSerializer(serializers.ModelSerializer):
    
	books = serializers.SerializerMethodField()
	books_write = serializers.CharField(write_only=True, required=False)
 
	class Meta:
		model = Author 
		fields = ('id', 'name', 'surname', 'patronymic', 'books', 'books_write')

	def get_books(self, obj):
		return [
			{
				'id': entry.id,
				'name': entry.name,
				'co-authors': [f"{i.name} (id={i.id})" for i in entry.authors.exclude(id=obj.id)]
			} for entry in obj.books.all()
		]
  
	def create(self, serializer):
     
		book_ids = serializer.pop('books_write').split(',')
		book_qs = Book.objects.filter(id__in=book_ids)
		author_obj = Author.objects.create(**serializer)
		author_obj.books.set(book_qs); author_obj.save()
		return author_obj
     