from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('name',)
