from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['name', 'details']
    fields = [
        'name',
        'email',
        'phone_number',
        'service',
        'details',
        'budget',
        'deadline',
        'attached',
        'attached_tag',
        'ordered_at',
    ]
    list_filter = ['service']
    list_display = ['name', 'ordered_at']
    readonly_fields = ['attached_tag', 'ordered_at']
