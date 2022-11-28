from django.contrib import admin 
from django.utils.translation import gettext_lazy as _ 

from .models import Book 

class CenturyListFilter(admin.SimpleListFilter):
    """List filter class for filtering Books based on the century they were 
    written in."""
    
    title = _('Century')
    parameter_name = 'century'
    
    def lookups(self, request, model_admin):
        return (
            ('19', _('19th')),
            ('20', _('20th')),
            ('21', _('21st'))
        )
        
    def queryset(self, request, queryset):
        
        if self.value():        
            return queryset.filter(
                year_of_publication__gte=(int(self.value()) - 1) * 100,
                year_of_publication__lte=(int(self.value()) * 100)
            )
    