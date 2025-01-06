from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_price', 'end_time')
    search_fields = ('name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'price')
    autocomplete_fields = ('product', 'user')
    date_hierarchy = "date"
