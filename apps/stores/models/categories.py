from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Base


class Category(Base):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class SubCategory(Base):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = _('Sub categories')

    def __str__(self):
        return self.name


class Tag(Base):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name
