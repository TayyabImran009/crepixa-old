from django import template
from django.core.files import storage

register = template.Library()


@register.simple_tag
def storage_url(media_url: str) -> str:
    if media_url:
        if media_url.startswith('http'):
            return media_url
        return storage.default_storage.url(media_url)
