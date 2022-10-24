from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.utils import get_file_path


class Order(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phone_number = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField(max_length=5000)
    budget = models.CharField(max_length=500)
    deadline = models.DateField(null=True, blank=True)
    attached = models.ImageField(null=True, blank=True, upload_to=get_file_path)

    service = models.ForeignKey(
        'services.Service',
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True, blank=True,
    )
    ordered_at = models.DateTimeField(default=timezone.now)

    def attached_tag(self):
        if self.attached:
            return mark_safe(f'<img width="150" height="auto" src="{self.attached.url}"/>')

    attached_tag.short_description = _('Attached image preview')

    def __str__(self):
        return self.name
