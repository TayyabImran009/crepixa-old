from django.contrib import admin

from csvexport.actions import csvexport
from modeltranslation.admin import TabbedTranslationAdmin

from core.admin import ConceptAdmin

from .models import (
    Slider, SocialMediaPage, CompanyInfo, BlogPage, ServicePage,
    PortfolioPage, ServiceOrderSection, Subscriber, StorePage, AboutUsSection,
)


@admin.register(Slider)
class SliderAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = [
        'is_active', 'ordering_number', 'bg_image', 'bg_image_tag',
        'title', 'subtitle', 'button_text', 'button_link',
    ]
    list_display = ('title', 'bg_image_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ('bg_image_tag',)


@admin.register(SocialMediaPage)
class SocialMediaPageAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')


@admin.register(CompanyInfo)
class CompanyInfoAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('address',)
    fields = ['company_name', 'address', 'city_country', 'phone_number', 'email_address']


@admin.register(PortfolioPage)
class PortfolioPageAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('title',)


@admin.register(StorePage)
class StorePageAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('title',)


@admin.register(BlogPage)
class BlogPageAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('title',)


@admin.register(ServicePage)
class ServicePageAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('title',)


@admin.register(ServiceOrderSection)
class ServiceOrderSectionAdmin(TabbedTranslationAdmin, ConceptAdmin):
    group_fieldsets = True
    list_display = ('subtitle',)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    actions = [csvexport]


@admin.register(AboutUsSection)
class AboutUsSectionAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('section_type', 'title', 'bg_image_tag', 'is_active', 'ordering_number')
    readonly_fields = ('bg_image_tag',)
