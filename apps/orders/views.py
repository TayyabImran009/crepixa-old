from contextlib import suppress
from datetime import datetime

from django.http import JsonResponse
from django.views.generic import TemplateView, FormView
from django.utils.translation import gettext_lazy as _

from services.models import Service
from .models import Order
from .forms import OrderForm, OrderCheckForm


class PlaceView(TemplateView):
    template_name = 'orders/place.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)

        context['page_title'] = _('Blog')
        context['meta_description'] = _('''meta description''')

        context['services'] = Service.pobs.all()
        return context


class OrderCheckView(FormView):
    form_class = OrderCheckForm

    def form_valid(self, form):
        return JsonResponse({}, status=200)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class OrderView(FormView):
    form_class = OrderForm

    def form_valid(self, form):
        o = Order(
            email=form.cleaned_data['email'],
            name=form.cleaned_data['name'],
            phone_number=form.cleaned_data['phone_number'],
            attached=form.cleaned_data['attached'],
            details=form.cleaned_data['details'],
            service=form.cleaned_data['service'],
            budget=form.cleaned_data['budget'] + " " + self.request.POST.get('currency'),
        )

        with suppress(Exception):
            o.deadline = datetime.strptime(self.request.POST.get('deadline'), '%Y-%m-%d').date()

        o.save()

        return JsonResponse({}, status=200)

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
