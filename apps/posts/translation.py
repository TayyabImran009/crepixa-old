from modeltranslation.translator import translator, TranslationOptions

from .models import Post, Category, Section


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'author_full_name')


class SectionTranslationOptions(TranslationOptions):
    fields = ('section_text',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Section, SectionTranslationOptions)
