from modeltranslation.translator import translator, TranslationOptions

from .models import Category, SubCategory, Tag, Store, StoreFeature


class StoreTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'label_text')


class StoreFeatureTranslationOptions(TranslationOptions):
    fields = ('feature_text',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Store, StoreTranslationOptions)
translator.register(StoreFeature, StoreFeatureTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(SubCategory, SubCategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)
