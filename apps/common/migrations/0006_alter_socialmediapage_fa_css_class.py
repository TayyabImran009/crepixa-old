# Generated by Django 4.0.2 on 2022-04-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_subscriber_remove_socialmediapage_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediapage',
            name='fa_css_class',
            field=models.CharField(choices=[('fa-behance', 'Behance'), ('fa-facebook-f', 'Facebook'), ('fa-telegram-plane', 'Telegram'), ('fa-youtube', 'Youtube'), ('fa-twitter', 'Twitter'), ('fa-instagram', 'Instagram'), ('fa-tiktok', 'TikTok'), ('fa-pinterest-p', 'Pinterest'), ('fa-whatsapp', 'Whatsapp'), ('fa-linkedin-in', 'Linkedin'), ('fa-dribbble', 'Dribbble')], max_length=100),
        ),
    ]
