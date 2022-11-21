from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrederAdmin(admin.ModelAdmin):
    list_display = ["book", "user", "created_at", "end_at", "plated_end_at"]