from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base, Button
from core.utils import get_file_path


class Slider(Base, Button):
    bg_image = models.ImageField(upload_to=get_file_path)
    title = models.CharField(max_length=500)
    subtitle = models.TextField()

    def bg_image_tag(self):
        if self.bg_image:
            return mark_safe(f'<img width="300" height="auto" src="{self.bg_image.url}"/>')

    bg_image_tag.short_description = _('Background image preview')
