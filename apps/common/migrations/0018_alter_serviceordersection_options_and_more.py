# Generated by Django 4.0.2 on 2022-06-28 18:42

import core.utils.utils
import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_companyinfo_company_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceordersection',
            options={'verbose_name_plural': '"Order Now" Section'},
        ),
        migrations.AlterField(
            model_name='aboutussection',
            name='bg_image',
            field=models.ImageField(blank=True, help_text='Use this only with `image with text` or `full-width image` section types', null=True, upload_to=core.utils.utils.get_file_path),
        ),
        migrations.AlterField(
            model_name='aboutussection',
            name='button_link',
            field=models.CharField(blank=True, help_text="If it is a link to an external page, please start with http:// or https://. If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.", max_length=500, null=True, validators=[core.validators.button_link_validator]),
        ),
        migrations.AlterField(
            model_name='serviceordersection',
            name='button_link',
            field=models.CharField(help_text="If it is a link to an external page, please start with http:// or https://. If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.", max_length=500, validators=[core.validators.button_link_validator]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='button_link',
            field=models.CharField(help_text="If it is a link to an external page, please start with http:// or https://. If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.", max_length=500, validators=[core.validators.button_link_validator]),
        ),
    ]