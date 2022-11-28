from django.contrib import admin 
from django.utils.translation import gettext_lazy as _

from .models import Author


class HasBooksListFilter(admin.SimpleListFilter):
    """Utility class for filtering Authors by their m2m 'books' field"""
    
    title = _('has_books')
    parameter_name = 'has_books'
    
    def lookups(self, request, model_admin):
        return (
            ('y', _('Yes')),
            ('n', _('No'))
        )
     
    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(
                books=None 
            )
            
        elif self.value() == 'n':
            return queryset.filter(
                books=None
            )

    
