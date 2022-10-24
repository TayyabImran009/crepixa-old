from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from core.models import Base
from core.utils import get_file_path


class Service(Base):
    icon = models.FileField(upload_to=get_file_path)
    name = models.CharField(max_length=500)

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Service(Homepage)')
        verbose_name_plural = _('Services(Homepage)')

    def icon_tag(self):
        if self.icon:
            return mark_safe(f'<img width="150" height="auto" src="{self.icon.url}"/>')

    icon_tag.short_description = _('Icon preview')


class Category(Base):
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class ServiceSlider(Base):
    image = models.FileField(upload_to=get_file_path)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title or "Untitled"

    class Meta:
        verbose_name = _('Service Slider')
        verbose_name_plural = _('Services Slider')

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img width="150" height="auto" src="{self.image.url}"/>')

    image_tag.short_description = _('Image preview')


class ServiceItem(Base):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)
    most_popular = models.CharField(max_length=100, null=True, blank=True)
    icon = models.FileField(upload_to=get_file_path)
    label = models.CharField(max_length=200, blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class Package(Base):
    title = models.CharField(max_length=200)
    price_currency = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    price_small = models.CharField(max_length=200, blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')


class ServiceItemFeature(models.Model):
    name = models.CharField(max_length=200)

    service_item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')


class PackageFeature(models.Model):
    name = models.CharField(max_length=200)

    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')


class Product(Base):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    price = models.CharField(max_length=200)
    icon = models.FileField(upload_to=get_file_path)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
