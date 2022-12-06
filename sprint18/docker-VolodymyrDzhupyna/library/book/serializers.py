from rest_framework import serializers
from .models import Book

from author.models import Author


class BookSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.SerializerMethodField()
    author_write = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Book
        fields = ("id", "url", "name", "description", "year_of_publication",
                  "author", "author_write")

    def get_author(self, obj):
        return  [f"{i.name} {i.surname}" for i in obj.authors.all()]
    
    def create(self, serializer):
        author_ids = serializer.pop('author_write').split(',')
        author_qs = Author.objects.filter(id__in=author_ids)
        book_obj = Book.objects.create(**serializer)
        book_obj.authors.set(author_qs); book_obj.save()
        return book_obj
