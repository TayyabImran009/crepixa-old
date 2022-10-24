from django.conf import settings as django_settings

from accounts.forms import SignupForm
from common.models import CompanyInfo, ServiceOrderSection, SocialMediaPage


def company_info(_):
    return {'ci': CompanyInfo.objects.first()}


def service_order(_):
    return {'si': ServiceOrderSection.objects.first()}


def settings(_):
    return {'settings': django_settings}


def forms(_):
    return {'signup_form': SignupForm()}


def social_media(_):
    return {'social_media_pages': SocialMediaPage.pobs.all()}
