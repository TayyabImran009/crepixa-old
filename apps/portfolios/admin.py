from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Category, SubCategory, Tag, Portfolio, PortfolioHomePage, PortfolioFile


class PortfolioFileInline(admin.StackedInline):
    extra = 0
    min_num = 1
    initial_num = 1
    model = PortfolioFile
    readonly_fields = ['portfolio_file_tag']


@admin.register(PortfolioHomePage)
class PortfolioHomePageAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']
    list_display = ('image_tag', 'is_active', 'ordering_number')


@admin.register(Portfolio)
class PortfolioAdmin(TabbedTranslationAdmin):
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
        'project_date',
        'categories',
        'sub_categories',
        'tags',
    ]
    list_display = ('title', 'thumbnail_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ['thumbnail_tag']
    inlines = [PortfolioFileInline]


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
