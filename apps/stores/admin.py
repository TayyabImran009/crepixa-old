from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from .models import StoreFeature, Category, SubCategory, Tag, Store


class StoreFeatureInline(TranslationStackedInline):
    extra = 0
    min_num = 1
    initial_num = 1
    model = StoreFeature


@admin.register(Store)
class StoreAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = [
        'is_active',
        'ordering_number',
        'title',
        'subtitle',
        'description',
        'thumbnail',
        'thumbnail_tag',
        'url_slug',
        'label_color',
        'label_text',
        'project_date',
        'categories',
        'sub_categories',
        'tags',
    ]
    list_display = ('title', 'thumbnail_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ['thumbnail_tag']
    inlines = [StoreFeatureInline]


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')


@admin.register(SubCategory)
class SubCategoryAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')


@admin.register(Tag)
class TagCategoryAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')
