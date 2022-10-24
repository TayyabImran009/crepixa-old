from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import translation
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base
from core.utils import get_file_path


class Category(Base):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Post(Base):
    title = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to=get_file_path)
    author_full_name = models.CharField(max_length=500, null=True, blank=True)
    url_slug = models.CharField(max_length=500, unique=True)
    posted_at = models.DateTimeField()
    categories = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'slug': self.url_slug})

    def thumbnail_tag(self):
        if self.thumbnail:
            return mark_safe(f'<img width="150" height="auto" src="{self.thumbnail.url}"/>')

    thumbnail_tag.short_description = _('Thumbnail preview')

    @staticmethod
    def title_lang():
        lang = translation.get_language()
        field_name = 'title'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name

    @staticmethod
    def author_full_name_lang():
        lang = translation.get_language()
        field_name = 'author_full_name'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name

    def __str__(self):
        return self.title


class Section(Base):
    FULL_WIDTH_IMAGE = 'f'
    IMAGE = 'i'
    TEXT = 't'
    SECTION_TYPES = (
        (FULL_WIDTH_IMAGE, _('Full width image')),
        (IMAGE, _('Image with paddings')),
        (TEXT, _('Text')),
    )
    section_type = models.CharField(choices=SECTION_TYPES, max_length=1)
    section_text = models.TextField(blank=True, null=True)
    section_image = models.ImageField(null=True, blank=True, upload_to=get_file_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_type

    def section_image_tag(self):
        if self.section_image:
            return mark_safe(f'<img width="150" height="auto" src="{self.section_image.url}"/>')
        return '-'

    section_image_tag.short_description = _('Section image preview')

    @staticmethod
    def section_text_lang():
        lang = translation.get_language()
        field_name = 'section_text'
        if lang != settings.LANGUAGE_CODE:
            field_name += '_' + lang

        return field_name
