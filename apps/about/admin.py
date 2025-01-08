from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Text)
class TextAdmin(TranslationAdmin, SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('text_type',)


@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ('order', 'name', 'status')
    list_display_links = ('name',)
    list_editable = ('order', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject', 'date')
    list_filter = ('subject',)
    search_fields = ('name',)
    autocomplete_fields = ('subject',)
    date_hierarchy = "date"
