from django.contrib import admin
from .models import Author
from book.models import Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "patronymic", "get_book"]

    @admin.display(description='Books')
    def get_book(self, obj):
        return [item.name for item in obj.books.all()]
