from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login as django_login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

import core.views.mixins
import accounts.forms
import accounts.models
import accounts.utils


__all__ = (
    'LoginView',
    'SignupView',
    'ConfirmEmailView',
    'ForgotPasswordView',
    'ResetPasswordView',
    'ProfileView',
    'ChangeProfileView',
    'ChangePasswordView',
    'DeleteAccountView',
)


class LoginView(core.views.mixins.AnonymousRequiredMixin, core.views.mixins.LoginRedirectMixin, generic.FormView):
    template_name = 'accounts/login.html'
    form_class = accounts.forms.LoginForm
    http_method_names = ['post']

    def form_valid(self, form):
        user, remember_me = form.cleaned_data
        django_login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        if not remember_me:
            self.request.session.set_expiry(0)
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class SignupView(core.views.mixins.AnonymousRequiredMixin, generic.FormView):
    model = get_user_model()
    http_method_names = ['post']
    form_class = accounts.forms.SignupForm

    def form_valid(self, form):
        user = form.save()
        accounts.utils.send_email_address_confirmation(user)
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class ConfirmEmailView(core.views.mixins.LoginRedirectMixin, generic.View):
    queryset = accounts.models.User.objects.all()

    # noinspection PyUnusedLocal
    def get(self, request, *args, **kwargs):
        token = request.GET.get('email_confirmation_token')
        if not token:
            raise Http404

        user = self.queryset.filter(email_confirmation_token=token).first()
        if not user:
            raise Http404

        user.is_active = True
        user.email_confirmation_token = None
        user.save()

        return JsonResponse({'success': True})


class ForgotPasswordView(core.views.mixins.AnonymousRequiredMixin, generic.FormView):
    form_class = accounts.forms.ForgotPasswordForm

    def form_valid(self, form):
        user = form.set_token()

        if user:
            accounts.utils.send_forgot_password_request(user)
            self.request.session['email_address'] = user.email
            self.request.session.save()

        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class ConfirmTokenView(core.views.mixins.LoginRedirectMixin, generic.FormView):
    form_class = accounts.forms.ConfirmTokenForm
    queryset = accounts.models.User.objects.all()

    def form_valid(self, _):
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


class ResetPasswordView(core.views.mixins.LoginRedirectMixin, generic.FormView):
    form_class = accounts.forms.ResetPasswordForm
    queryset = accounts.models.User.objects.all()

    def dispatch(self, request, *args, **kwargs):
        token = request.POST.get('token')
        if not token:
            raise Http404

        user = self.queryset.filter(reset_password_token=token).first()
        if not user:
            raise Http404

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        token = self.kwargs.get('token')
        user = form.change_password(token)
        if user:
            django_login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return JsonResponse({'success': True})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class ProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/profile.html'
    form_class = accounts.forms.AccountForm
    model = accounts.models.User
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(csrf_exempt, name='dispatch')
class ChangeProfileView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/change_profile.html'
    form_class = accounts.forms.AccountForm
    model = accounts.models.User
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        valid = super(ChangeProfileView, self).form_valid(form)
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Profile updated.')
        return valid


@method_decorator(csrf_exempt, name='dispatch')
class ChangePasswordView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/change_profile.html'
    form_class = accounts.forms.ChangePasswordForm
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context['password_form'] = context['form']
        context['form'] = accounts.forms.AccountForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        valid = super(ChangePasswordView, self).form_valid(form)
        update_session_auth_hash(self.request, self.request.user)
        messages.success(self.request, 'Your password has been change!')
        return valid


@method_decorator(csrf_exempt, name='dispatch')
class DeleteAccountView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('common:homepage')

    def get_object(self, queryset=None):
        return self.request.user
