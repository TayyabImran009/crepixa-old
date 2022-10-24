from django.contrib import sitemaps
from django.urls import reverse

__all__ = (
    'StaticViewSitemap',
)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return [
            'common:homepage', 'common:about', 'common:contact_us',
        ]

    def location(self, item):
        return reverse(item)
