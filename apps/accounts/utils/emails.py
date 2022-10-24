from django.conf import settings
from django.urls import reverse

from core.email.utils import send_email
from core.utils.utils import build_client_absolute_url

__all__ = (
    'send_email_address_confirmation',
    'send_forgot_password_request',
)


def send_email_address_confirmation(user):
    email_confirmation_path = reverse('common:homepage')
    email_confirmation_path += '?ect={}'.format(user.email_confirmation_token)

    subject = 'Confirm your registration at {site_name}'.format(
        site_name=settings.SITE_NAME
    )

    send_email(
        subject=subject,
        template_name='accounts/emails/email_address_confirmation.html',
        context={
            'email_confirmation_url': build_client_absolute_url(email_confirmation_path),
        },
        to=user.email,
    )


def send_forgot_password_request(user):
    reset_password_token_path = reverse('common:homepage')
    reset_password_token_path += '?rpt={}'.format(user.reset_password_token)

    subject = 'Reset your {site_name} password'.format(
        site_name=settings.SITE_NAME
    )

    send_email(
        subject=subject,
        template_name='accounts/emails/forgot_password_request.html',
        context={
            'reset_password_url': build_client_absolute_url(reset_password_token_path),
            'full_name': user.get_full_name(),
        },
        to=user.email,
    )
