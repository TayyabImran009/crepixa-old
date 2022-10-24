from urllib.parse import urlparse

from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import translation
from django.views import generic
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from common.utils import contact_us_notification
from portfolios.models import PortfolioHomePage
from testimonials.models import Testimonial
from services.models import Service
from .forms import ContactForm, SubscriberFrom
from .models import Slider, ServiceOrderSection, Subscriber, AboutUsSection


class HomePageView(TemplateView):
    template_name = 'common/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        context['page_title'] = _('Homepage')
        context['meta_description'] = _('''meta description''')

        context['slides'] = Slider.pobs.all()
        context['testimonials'] = Testimonial.pobs.all()
        context['services'] = Service.pobs.all()
        context['service_order'] = ServiceOrderSection.objects.first()
        context['portfolios'] = PortfolioHomePage.pobs.all()

        return context


class SwitchLanguageView(generic.RedirectView):
    def get(self, *args, **kwargs):
        response = super().get(*args, **kwargs)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, translation.get_language())
        return response

    def get_redirect_url(self, *args, **kwargs):
        language_code = self.request.GET.get('code', settings.LANGUAGE_CODE)
        if language_code in [l[0] for l in settings.LANGUAGES]:
            translation.activate(language_code)

        referer = self.request.META.get('HTTP_REFERER', f'/{language_code}/')

        path = urlparse(referer).path

        for code, _ in settings.LANGUAGES:
            path = path.replace(f'/{code}/', '/')

        if language_code != settings.LANGUAGE_CODE:
            path = f'/{language_code}{path}'

        if not path.endswith('/'):
            path += '/'

        return path


class AboutPageView(generic.TemplateView):
    template_name = 'common/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['page_title'] = _('About')
        context['meta_description'] = _('''meta description''')

        context['sections'] = AboutUsSection.pobs.all()
        context['Section'] = AboutUsSection
        return context


class ContactPageView(generic.FormView):
    template_name = 'common/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('common:homepage')

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['page_title'] = _('Contact')
        context['meta_description'] = _('''meta description''')
        return context

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        contact_us_notification(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['message'],
        )
        return JsonResponse({}, status=200)


class SubscribeView(generic.View):
    def post(self, request, *args, **kwargs):
        subscriber_form = SubscriberFrom(request.POST)
        if subscriber_form.is_valid():
            _, _ = Subscriber.objects.get_or_create(email=subscriber_form.cleaned_data['email'])
            return JsonResponse({'success': True}, status=201)
        return JsonResponse({'success': False}, status=400)


class PrivacyPolicyView(generic.TemplateView):
    template_name = 'common/privacy.html'


class CookiesView(generic.TemplateView):
    template_name = 'common/cookies.html'


class TermsView(generic.TemplateView):
    template_name = 'common/terms.html'


class ImpressumView(generic.TemplateView):
    template_name = 'common/impressum.html'
