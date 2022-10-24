import django.core.exceptions
from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse

__all__ = (
    'AnonymousRequiredMixin',
    'LoginRedirectMixin',
    'MetaDescriptionViewMixin',
)


class AnonymousRequiredMixin(AccessMixin):
    """Verifies that request is anonymous."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:profile')
        return super().dispatch(request, *args, **kwargs)


class LoginRedirectMixin(AccessMixin):
    def get_redirect_url(self):
        redirect_url = self.request.GET.get(
            self.redirect_field_name,
            reverse('common:homepage'),
        )
        return redirect_url


class MetaDescriptionViewMixin:
    """
    Provides ``meta_description`` variable to template context.
    """

    meta_description = None

    def get_meta_description(self):
        if self.meta_description is None:
            raise django.core.exceptions.ImproperlyConfigured('meta_description attribute is not specified.')
        return self.meta_description

    def get_context_data(self, **kwargs):
        kwargs['meta_description'] = self.get_meta_description()
        # noinspection PyUnresolvedReferences
        return super(MetaDescriptionViewMixin, self).get_context_data(**kwargs)


class AjaxFormViewMixin:
    # noinspection PyMethodMayBeStatic, PyUnusedLocal
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()

            after_save = getattr(self, 'after_save', None)
            if after_save and callable(after_save):
                after_save()

            return HttpResponse(status=204)
        else:
            return JsonResponse(form.errors, status=400)
