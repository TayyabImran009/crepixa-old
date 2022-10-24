from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base
from core.utils import get_file_path


class Testimonial(Base):
    logo = models.ImageField(upload_to=get_file_path)
    name = models.CharField(max_length=500)
    job_description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.name

    def logo_tag(self):
        if self.logo:
            return mark_safe(f'<img width="150" height="auto" src="{self.logo.url}"/>')

    logo_tag.short_description = _('Logo preview')
