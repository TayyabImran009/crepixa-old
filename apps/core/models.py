from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import translation

from .managers import BaseManager
from .validators import button_link_validator


class IsActive(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class OrderingNumber(models.Model):
    ordering_number = models.IntegerField(help_text=_('Ascending'))

    class Meta:
        abstract = True


class Base(IsActive, OrderingNumber):
    """
    BaseModel is a joined version of IsActive and OrderingNumber models.
    """
    # ordered public objects only
    objects = models.Manager()
    pobs = BaseManager()

    class Meta:
        abstract = True


class Button(models.Model):
    """
    Button is a model that has a button_text field and button_url field.
    """
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(
        max_length=500,
        validators=[button_link_validator],
        help_text=_('''If it is a link to an external page, please start with http:// or https://. If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.'''))

    @property
    def button_url(self):
        if self.button_link.startswith('http://') or self.button_link.startswith('https://'):
            return self.button_link

        lang = translation.get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.button_link

        return f'/{lang}' + self.button_link

    @property
    def is_button_external(self):
        return self.button_link.startswith('http://') or self.button_link.startswith('https://')

    def __str__(self):
        return self.button_text

    class Meta:
        abstract = True
