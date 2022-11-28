from django.contrib import admin

from .models import Book
from author.models import Author
from .filters import CenturyListFilter

class AuthorInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ['name', 'get_author', 'year_of_publication', 'count', 'in_stock']
    list_filter = [
        'in_stock',
        ('authors', admin.RelatedOnlyFieldListFilter),
        CenturyListFilter
    ]
    readonly_fields = ['name', 'description', 'year_of_publication']

    fieldsets = (
        ("Book info (read-only)", {
            "fields": (
                'name', 'description', 'year_of_publication'
            ),
            "description": "<h3>General info about the book itself.</h3><hr>"
        }),
        ('Availability', {
            "fields": (
                'count', 'in_stock'
            ),
            "description": "<h3>Describes how many specimens of the book left " \
                           "in the library.</h3><hr>"
        }),
    )

    ordering = ('-count', )
    search_fields = ['id', 'name']
    inlines = [
        AuthorInline,
    ]

    def get_author(self, obj):
        return [f"{i.name} {i.surname}" for i in obj.authors.all()]

    get_author.short_description = 'Author(s)'
