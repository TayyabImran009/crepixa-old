from modeltranslation.translator import translator, TranslationOptions

from .models import (
    Slider, SocialMediaPage, Shortcut, CompanyInfo, PortfolioPage,
    ServiceOrderSection, StorePage, BlogPage, ServicePage, AboutUsSection,
)


class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'button_text')


class SocialMediaPageTranslationOptions(TranslationOptions):
    fields = ('name',)


class ShortcutTranslationOptions(TranslationOptions):
    fields = ('text',)


class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('city_country', 'address', 'phone_number', 'email_address')


class PortfolioPageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class StorePageTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class ServicePageTranslationOption(TranslationOptions):
    fields = ('title',)


class BlogPageTranslationOption(TranslationOptions):
    fields = ('title', 'subtitle')


class ServiceOrderSectionTranslationOptions(TranslationOptions):
    fields = ('button_text', 'subtitle')


class AboutUsSectionTranslationOptions(TranslationOptions):
    fields = ('button_text', 'title', 'description')


translator.register(Slider, SliderTranslationOptions)
translator.register(SocialMediaPage, SocialMediaPageTranslationOptions)
translator.register(Shortcut, ShortcutTranslationOptions)
translator.register(CompanyInfo, CompanyInfoTranslationOptions)
translator.register(PortfolioPage, PortfolioPageTranslationOptions)
translator.register(StorePage, StorePageTranslationOptions)
translator.register(ServicePage, ServicePageTranslationOption)
translator.register(BlogPage, BlogPageTranslationOption)
translator.register(ServiceOrderSection, ServiceOrderSectionTranslationOptions)
translator.register(AboutUsSection, AboutUsSectionTranslationOptions)
