# Generated by Django 4.0.2 on 2022-04-13 06:33

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_socialmediapage_fa_css_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceordersection',
            name='button_link',
            field=models.URLField(help_text="\n            If it is a link to an external page, please start with http:// or https://.\n            If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.\n        ", validators=[core.validators.button_link_validator]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='button_link',
            field=models.URLField(help_text="\n            If it is a link to an external page, please start with http:// or https://.\n            If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.\n        ", validators=[core.validators.button_link_validator]),
        ),
    ]
