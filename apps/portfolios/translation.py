from modeltranslation.translator import translator, TranslationOptions

from .models import Category, SubCategory, Tag, Portfolio


class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Portfolio, PortfolioTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(SubCategory, SubCategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
