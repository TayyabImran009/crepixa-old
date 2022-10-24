from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(TabbedTranslationAdmin):
    group_fieldsets = True
    fields = [
        'is_active', 'ordering_number', 'name', 'logo', 'logo_tag',
        'job_description', 'review',
    ]
    list_display = ('name', 'logo_tag', 'is_active', 'ordering_number')
    list_filter = ['is_active']
    readonly_fields = ['logo_tag']
