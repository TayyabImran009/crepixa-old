from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import translation
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base
from core.utils import get_file_path

from .categories import Category, SubCategory, Tag


class Store(Base):
    LABEL_COLOR_CHOICES = (
        ('black', _('Black')),
        ('red', _('Red')),
    )

    thumbnail = models.ImageField(upload_to=get_file_path)
    project_date = models.DateField(null=True)
    url_slug = models.CharField(max_length=500, unique=True)
    title = models.CharField(max_length=500)
    subtitle = models.TextField()
    description = models.TextField()
    label_color = models.CharField(max_length=10, choices=LABEL_COLOR_CHOICES, null=True, blank=True)
    label_text = models.CharField(max_length=50, null=True, blank=True)

    categories = models.ManyToManyField(Category)
    sub_categories = models.ManyToManyField(SubCategory)
    tags = models.ManyToManyField(Tag)

    @staticmethod
    def title_lang():
        lang = translation.get_language()
        field_name = 'title'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name

    @staticmethod
    def subtitle_lang():
        lang = translation.get_language()
        field_name = 'subtitle'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name

    @staticmethod
    def description_lang():
        lang = translation.get_language()
        field_name = 'description'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name

    def get_absolute_url(self):
        return reverse('stores:store', kwargs={'slug': self.url_slug})

    def thumbnail_tag(self):
        if self.thumbnail:
            return mark_safe(f'<img width="150" height="auto" src="{self.thumbnail.url}"/>')

    thumbnail_tag.short_description = _('Thumbnail preview')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Store Item')
        verbose_name_plural = _('Store Items')


class StoreFeature(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    feature_text = models.CharField(max_length=500)

    def __str__(self):
        return self.feature_text

    class Meta:
        verbose_name = _('Store Item Feature')
        verbose_name_plural = _('Store Item Features')

    @staticmethod
    def feature_text_lang():
        lang = translation.get_language()
        field_name = 'feature_text'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name
