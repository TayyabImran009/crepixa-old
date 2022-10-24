from django.core.management.base import BaseCommand

from common.models import CompanyInfo, PortfolioPage, ServiceOrderSection, StorePage, BlogPage, ServicePage


class Command(BaseCommand):
    help = 'Creates minimal objects that needed.'

    def handle(self, *args, **options):
        if not CompanyInfo.objects.all().exists():
            _ = CompanyInfo.objects.create(
                city_country='city, country',
                address='address',
                phone_number='888888888',
                email_address='email@example.com',
            )
        if not PortfolioPage.objects.all().exists():
            _ = PortfolioPage.objects.create(
                title='portfolio title',
                subtitle='portfolio subtitle',
            )
        if not StorePage.objects.all().exists():
            _ = StorePage.objects.create(
                title='store title',
                subtitle='store subtitle',
            )
        if not BlogPage.objects.all().exists():
            _ = BlogPage.objects.create(
                title='blog title',
                subtitle='blog subtitle',
            )
        if not ServicePage.objects.all().exists():
            _ = ServicePage.objects.create(
                title='Service title',
            )
        if not ServiceOrderSection.objects.all().exists():
            _ = ServiceOrderSection.objects.create(
                button_text='Order a service',
                subtitle='order a service subtitle',
            )
