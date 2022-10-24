from django.conf import settings
from django.utils.translation import gettext_lazy as _

from core.email.utils import send_email


def contact_us_notification(**kwargs):
    send_email(
        subject=_('Contact Us Notification'),
        template_name='common/emails/contact_us.html',
        context=kwargs,
        to=settings.ADMIN_EMAILS,
    )
