from django.core.exceptions import ValidationError


def button_link_validator(value):
    if not value.startswith('http://') and not value.startswith('https://') and not value.startswith('/'):
        raise ValidationError('Link must start with http:// https:// or /')
