from django.contrib import admin

from .models import Author
from book.models import Book
from .filters import HasBooksListFilter


class BookInline(admin.TabularInline):
    model = Author.books.through
    extra = 1
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'book']
    readonly_fields = ['name', 'surname', 'patronymic']
    list_filter = ['books', HasBooksListFilter]

    fieldsets = (
        ("Personal Info (read-only)", {
            "fields": (
                'name', 'surname', 'patronymic'
            ),
        }),
    )

    inlines = [
        BookInline,
    ]

    def book(self, obj):
        return [i.name for i in obj.books.all()]

    book.short_description = "Books written"

    def full_name(self, obj):
        return f"{obj.name} {obj.surname} {obj.patronymic}"

    full_name.short_description = "Full name"
