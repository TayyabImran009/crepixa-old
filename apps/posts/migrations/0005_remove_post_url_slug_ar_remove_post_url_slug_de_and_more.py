# Generated by Django 4.0.2 on 2022-04-08 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url_slug_ar',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url_slug_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url_slug_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='url_slug_fr',
        ),
    ]
