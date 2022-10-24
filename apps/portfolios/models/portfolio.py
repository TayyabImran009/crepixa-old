from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base
from core.utils import get_file_path

from .categories import Category, SubCategory, Tag


class Portfolio(Base):
    thumbnail = models.ImageField(upload_to=get_file_path)
    project_date = models.DateField(null=True)
    url_slug = models.CharField(max_length=500, unique=True)
    title = models.CharField(max_length=500)
    subtitle = models.TextField()
    description = models.TextField()

    categories = models.ManyToManyField(Category)
    sub_categories = models.ManyToManyField(SubCategory)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse('portfolios:portfolio', kwargs={'slug': self.url_slug})

    def thumbnail_tag(self):
        if self.thumbnail:
            return mark_safe(f'<img width="150" height="auto" src="{self.thumbnail.url}"/>')

    thumbnail_tag.short_description = _('Thumbnail preview')

    def __str__(self):
        return self.title


class PortfolioFile(Base):
    portfolio_file = models.FileField(upload_to=get_file_path)
    title = models.CharField(max_length=500, null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def portfolio_file_tag(self):
        if self.portfolio_file:
            return mark_safe(f'<img width="150" height="auto" src="{self.portfolio_file.url}"/>')

    portfolio_file_tag.short_description = _('Portfolio file preview')


class PortfolioHomePage(Base):
    image = models.ImageField(upload_to=get_file_path)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img width="150" height="auto" src="{self.image.url}"/>')

    image_tag.short_description = _('Portfolio file preview')

    class Meta:
        verbose_name = _('Portfolio(Homepage)')
        verbose_name_plural = _('Portfolios(Homepage)')
