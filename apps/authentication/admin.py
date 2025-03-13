from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ordering = ['phone_number']  # Use 'phone_number' or another existing field
    list_display = ['phone_number', 'full_name', 'is_active', 'is_staff']  # Use existing fields
    search_fields = ['phone_number', 'full_name']  # Add search fields for autocomplete
