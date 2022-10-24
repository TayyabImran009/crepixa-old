from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from .models import Category, ServiceItem, ServiceSlider, Package, Product


class ServicesView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)

        context['page_title'] = _('Services')
        context['meta_description'] = _('''meta description''')

        context['services'] = ServiceItem.pobs.prefetch_related('serviceitemfeature_set')
        context['packages'] = Package.pobs.prefetch_related('packagefeature_set')
        context['sliders'] = ServiceSlider.pobs.all()
        context['categories'] = Category.pobs.all()
        context['products'] = Product.pobs.all()
        return context
