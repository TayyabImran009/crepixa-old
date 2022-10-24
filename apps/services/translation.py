from modeltranslation.translator import translator, TranslationOptions

from .models import (
    Service, Category, ServiceSlider, ServiceItem,
    ServiceItemFeature, PackageFeature, Package, Product,
)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class ServiceSliderTranslationOptions(TranslationOptions):
    fields = ('title',)


class ServiceItemFeatureTranslationOptions(TranslationOptions):
    fields = ('name',)


class PackageFeatureTranslationOptions(TranslationOptions):
    fields = ('name',)


class PackageTranslationOptions(TranslationOptions):
    fields = ('title', 'price', 'price_currency', 'price_small')


class ServiceItemTranslationOptions(TranslationOptions):
    fields = ('title', 'price', 'description', 'label')


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'price')


translator.register(Service, ServiceTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(ServiceSlider, ServiceSliderTranslationOptions)
translator.register(ServiceItemFeature, ServiceItemFeatureTranslationOptions)
translator.register(PackageFeature, PackageFeatureTranslationOptions)
translator.register(Package, PackageTranslationOptions)
translator.register(ServiceItem, ServiceItemTranslationOptions)
translator.register(Product, ProductTranslationOptions)
