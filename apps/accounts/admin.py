from django.contrib.auth import admin as user_admin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from accounts.models import User


@admin.register(User)
class UserAdmin(user_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'title', 'company_name', 'country', 'city', 'zip_code', 'street_house_no')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
