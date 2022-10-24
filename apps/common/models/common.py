from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base, Button
from core.utils import get_file_path
from core.validators import button_link_validator


class Shortcut(Base):
    text = models.CharField(max_length=500)
    link = models.URLField()

    def __str__(self):
        return self.text


class CompanyInfo(models.Model):
    logo = models.FileField(upload_to=get_file_path)
    company_name = models.CharField(max_length=150)
    city_country = models.CharField(max_length=500, help_text=_('Berlin, Germany'))
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email_address = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _('Company info(footer, contact us)')

    def __str__(self):
        return self.city_country


class PortfolioPage(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = _('Portfolio page(title, subtitle)')

    def __str__(self):
        return self.title


class StorePage(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = _('Store page(title, subtitle)')

    def __str__(self):
        return self.title


class BlogPage(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = _('Blog page(title, subtitle)')

    def __str__(self):
        return self.title


class ServicePage(models.Model):
    title = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = _('Service page(title)')

    def __str__(self):
        return self.title


class ServiceOrderSection(Button):
    subtitle = models.TextField()

    class Meta:
        verbose_name_plural = _('"Order Now" Section')

    def __str__(self):
        return self.subtitle


class AboutUsSection(Base, Button):
    FULL_WIDTH_IMAGE = 'full_width_image'
    TEXT = 'text'
    IMAGE_WITH_TEXT = 'image_with_text'
    SECTION_TYPES = (
        (FULL_WIDTH_IMAGE, _('Full width image')),
        (TEXT, _('Text')),
        (IMAGE_WITH_TEXT, _('Image with text')),
    )
    IMAGE_TYPE_LEFT = 'image_left'
    IMAGE_TYPE_TOP = 'image_top'
    IMAGE_TYPE_BOTTOM = 'image_bottom'
    IMAGE_TYPES = (
        (IMAGE_TYPE_LEFT, _('Image left')),
        (IMAGE_TYPE_TOP, _('Image top')),
        (IMAGE_TYPE_BOTTOM, _('Image bottom')),
    )
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)

    bg_image = models.ImageField(
        upload_to=get_file_path,
        blank=True, null=True,
        help_text=_('Use this only with `image with text` or `full-width image` section types'),
    )
    image_with_text_type = models.CharField(
        max_length=20, blank=True, null=True,
        choices=IMAGE_TYPES, help_text=_('Use this only with `image with text` section type'),
    )

    title = models.CharField(
        max_length=500, blank=True, null=True,
        help_text=_('Use this only with `text` or `image with text` section types'),
    )
    description = models.TextField(blank=True, null=True, help_text=_('Use this only with `text` section type'))

    button_text = models.CharField(max_length=100, null=True, blank=True)
    button_link = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        validators=[button_link_validator],
        help_text=_('''If it is a link to an external page, please start with http:// or https://. If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.'''))

    def __str__(self):
        return self.section_type

    def bg_image_tag(self):
        if self.bg_image:
            return mark_safe(f'<img width="300" height="auto" src="{self.bg_image.url}"/>')

    bg_image_tag.short_description = _('Background image preview')
