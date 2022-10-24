import secrets

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_countries.fields import CountryField

__all__ = (
    'User',
)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    TITLES = (
        ('mr', _('Mr.')),
        ('ms', _('Ms.')),
        ('div', _('Div.')),
    )
    email = models.EmailField(unique=True)
    email_confirmation_token = models.CharField(max_length=64, editable=False, null=True)

    reset_password_token = models.CharField(max_length=64, editable=False, null=True)
    reset_password_request_date = models.DateTimeField(null=True)

    title = models.CharField(choices=TITLES, max_length=3)
    company_name = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=500, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    street_house_no = models.CharField(max_length=100, null=True)
    country = CountryField(null=True)

    USERNAME_FIELD = 'email'
    username = None
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def generate_password_request_date(self):
        self.reset_password_request_date = timezone.now()

    @staticmethod
    def generate_token() -> str:
        return secrets.token_urlsafe()
