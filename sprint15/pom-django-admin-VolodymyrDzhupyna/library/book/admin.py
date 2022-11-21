from django.contrib import admin
from .models import Book
from author.models import Author


class MembershipInLine(admin.TabularInline):
    model = Author.books.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "count", "author", 'pub_year', 'issue_date']
    fieldsets = (
        ("Changeable fields", {"fields": ('issue_date', 'description', 'count')}),
        ("Read only fields", {"fields": ('name', 'pub_year')})
    )
    list_filter = ["id", "name", "authors"]

    inlines = [
        MembershipInLine,
    ]
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name', 'pub_year', 'authors')
        return self.readonly_fields

    def author(self, obj):
        return " ".join([item.name + " " + item.surname for item in obj.authors.all()])