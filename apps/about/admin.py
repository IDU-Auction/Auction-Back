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
