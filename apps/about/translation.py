from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('address',)


@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)
