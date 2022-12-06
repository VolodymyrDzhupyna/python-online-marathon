from django.contrib import admin 
from django.utils.translation import gettext_lazy as _ 

class IsOrderEndedListFilter(admin.SimpleListFilter):
    """
    SimpleListFilter-based class for enabling Order list filter on whether 
    they are ended or not. The relevance of this class lies in the fact that 
    Order objects don't have an 'is_ended' field.
    """
        
    title = _('is_ended')
    
    parameter_name = 'is_ended'
    
    def lookups(self, request, model_admin):
        return (
            ('y', _('Yes')),
            ('n', _('No'))
        )
        
    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(
                end_at=None
            )
            
        elif self.value() == 'n':
            return queryset.filter(
                end_at=None
            )