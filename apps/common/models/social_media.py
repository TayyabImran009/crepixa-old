from django.db import models

from core.models import Base


class SocialMediaPage(Base):
    FA_CSS_CLASSES = (
        ('fa-behance', 'Behance'),
        ('fa-facebook-f', 'Facebook'),
        ('fa-telegram-plane', 'Telegram'),
        ('fa-youtube', 'Youtube'),
        ('fa-twitter', 'Twitter'),
        ('fa-instagram', 'Instagram'),
        ('fa-tiktok', 'TikTok'),
        ('fa-pinterest-p', 'Pinterest'),
        ('fa-whatsapp', 'Whatsapp'),
        ('fa-linkedin-in', 'Linkedin'),
        ('fa-dribbble', 'Dribbble'),
    )
    fa_css_class = models.CharField(choices=FA_CSS_CLASSES, max_length=100)
    link = models.URLField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
