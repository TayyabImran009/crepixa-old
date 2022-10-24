from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from .models import Service, Category, ServiceSlider, Package, ServiceItem, ServiceItemFeature, PackageFeature, Product


class PackageFeatureInline(TranslationStackedInline):
    extra = 0
    min_num = 1
    initial_num = 1
    model = PackageFeature


class ServiceItemFeatureFeatureInline(TranslationStackedInline):
    extra = 0
    min_num = 1
    initial_num = 1
    model = ServiceItemFeature


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = ['is_active', 'ordering_number', 'name', 'category', 'icon', 'icon_tag']
    list_display = ('name', 'icon_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ('icon_tag',)


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')


@admin.register(ServiceSlider)
class ServiceSliderAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = [
        'is_active',
        'ordering_number',
        'title',
        'image',
        'image_tag',
    ]
    list_display = ('title', 'image_tag', 'is_active', 'ordering_number')
    readonly_fields = ['image_tag']


@admin.register(Package)
class PackageAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_filter = ['category']
    list_display = ('title', 'is_active', 'ordering_number')
    inlines = [PackageFeatureInline]


@admin.register(ServiceItem)
class ServiceItemAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_filter = ['category']
    list_display = ('title', 'is_active', 'ordering_number')
    inlines = [ServiceItemFeatureFeatureInline]


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_filter = ['category']
    list_display = ('title', 'is_active', 'ordering_number')
