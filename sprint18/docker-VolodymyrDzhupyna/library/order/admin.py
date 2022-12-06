from django.contrib import admin

from .models import Order
from .filters import IsOrderEndedListFilter
from authentication.models import CustomUser
from book.models import Book


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'plated_end_at', 'is_ended']
    list_filter = [
        ('book', admin.RelatedOnlyFieldListFilter),
        ('user', admin.RelatedOnlyFieldListFilter),
        IsOrderEndedListFilter
    ]
    readonly_fields = ['book', 'user', 'created_at', 'plated_end_at']
    search_fields = ['user__email', 'user__id', 'book__name', 'book__id']

    ordering = ['-created_at']

    fieldsets = (
        ("General order details", {
            "fields": (
                'book', 'user'
            ),
            "description": "<h3>Data about the user and the book he/she ordered.</h3><hr>"
        }),
        ("Order date info", {
            "fields": (
                'created_at', 'end_at', 'plated_end_at',

            ),
            'description': "<h3>All time-related info about the given order.</h3><hr>"
        })
    )


    def is_ended(self, obj):
        return obj.end_at != None

    is_ended.boolean = True
