from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_price', 'end_time', 'auction')
    list_filter = ('auction',)
    list_editable = ('auction',)
    search_fields = ('name',)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'price')
    autocomplete_fields = ('product', 'user')
    date_hierarchy = "date"
