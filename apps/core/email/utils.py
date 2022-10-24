from typing import List, Tuple, Union

from django.conf import settings
from django.template import loader
from django.core.mail import EmailMessage

from core.utils import build_client_absolute_url

__all__ = (
    'send_email',
)


Recipient_s = Union[List[str], Tuple[str], str]


def render_body(template_name: str, context: dict) -> str:
    """
    Load template by given name, pass it context
    and render as a string.
    """
    context['base_template'] = context.get('base_template', settings.EMAIL_BASE_TEMPLATE)
    context['base_url'] = build_client_absolute_url('')
    template = loader.get_template(template_name)
    return template.render(context)


def send_email(
    subject: str,
    template_name: str,
    to: Recipient_s,
    context: dict = None,
    bcc: Recipient_s = None,
    cc: Recipient_s = None,
    reply_to: Recipient_s = None,
):

    if not to:
        return  # pragma: no cover

    if not context:
        context = dict()

    context['subject'] = subject

    body = render_body(template_name, context)

    send_sync_email(
        subject=subject,
        body=body,
        to=to if isinstance(to, list) else [to],
        bcc=[bcc] if bcc else None,
        cc=[cc] if cc else None,
        reply_to=[reply_to] if reply_to else None,
    )


def send_sync_email(
    subject: str,
    body: str,
    to: List[str],
    bcc: List[str] = None,
    cc: List[str] = None,
    reply_to: List[str] = None,
):
    """Task for sending emails asynchronously"""
    email = EmailMessage(
        subject=subject,
        body=body,
        to=to,
        bcc=bcc,
        cc=cc,
        reply_to=reply_to,
    )

    # Setting main content
    email.content_subtype = 'html'

    email.send()
