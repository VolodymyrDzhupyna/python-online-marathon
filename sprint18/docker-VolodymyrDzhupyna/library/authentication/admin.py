from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
# Register your models here.

admin.site.unregister(Group)

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):

    list_display = ['email', 'role', 'is_superuser']
    list_filter = ['is_superuser', 'is_staff', 'is_active', 'role']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('last_name', 'first_name', 'middle_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'role')}),
    )
    
    add_fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        # (None, {'fields': ('email', 'password', 'role')})
    )

    search_fields = ['email', 'id']
    ordering = ['email']
    filter_horizontal = ()

# admin.site.register(CustomUser, UserAdmin)
