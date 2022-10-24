from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from .sitemaps import *  # noqa

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

admin.site.site_header = settings.SITE_NAME
admin.site.site_title = settings.SITE_NAME


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('common.urls', namespace='common')),
    path('blog/', include('posts.urls', namespace='posts')),
    path('portfolio/', include('portfolios.urls', namespace='portfolios')),
    path('store/', include('stores.urls', namespace='stores')),
    path('services/', include('services.urls', namespace='services')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('social-accounts/', include('allauth.urls')),
    prefix_default_language=False,
)

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

handler404 = 'core.handlers.handler404'
