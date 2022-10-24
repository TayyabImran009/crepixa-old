from django import template
from django.conf import settings

from core.utils import build_client_absolute_url

register = template.Library()


@register.inclusion_tag('core/opengraph/meta.html')
def opengraph_meta(request, site_name=None, title=None, image=None, description=None, **kwargs):
    if hasattr(image, 'url'):
        image = image.url
    if not site_name:
        site_name = settings.SITE_NAME
    if 'og_type' not in kwargs:
        kwargs['og_type'] = 'website'
    return {
        'url': build_client_absolute_url(request.path),
        'site_name': site_name,
        'title': title,
        'image': build_client_absolute_url(image) if image else None,
        'description': description,
        **kwargs,
    }
