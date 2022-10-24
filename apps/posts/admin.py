from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from .models import Post, Category, Section


class SectionInline(TranslationStackedInline):
    extra = 0
    min_num = 1
    initial_num = 1
    model = Section
    readonly_fields = ['section_image_tag']


@admin.register(Post)
class PostAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = [
        'is_active',
        'ordering_number',
        'title',
        'thumbnail',
        'thumbnail_tag',
        'author_full_name',
        'url_slug',
        'posted_at',
        'categories',
    ]
    list_display = ('title', 'thumbnail_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ['thumbnail_tag']
    inlines = [SectionInline]


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'is_active', 'ordering_number')
