# Generated by Django 4.0.2 on 2022-04-15 04:41

import core.utils.utils
import core.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_alter_companyinfo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('section_type', models.CharField(choices=[('full_width_image', 'Full width image'), ('text', 'Text'), ('image_with_text', 'Image with text')], max_length=20)),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to=core.utils.utils.get_file_path)),
                ('image_with_text_type', models.CharField(blank=True, choices=[('image_left', 'Image left'), ('image_top', 'Image top'), ('image_bottom', 'Image bottom')], max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('title_en', models.CharField(blank=True, max_length=500, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=500, null=True)),
                ('title_de', models.CharField(blank=True, max_length=500, null=True)),
                ('title_fr', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ar', models.TextField(blank=True, null=True)),
                ('description_de', models.TextField(blank=True, null=True)),
                ('description_fr', models.TextField(blank=True, null=True)),
                ('button_text', models.CharField(blank=True, max_length=100, null=True)),
                ('button_text_en', models.CharField(blank=True, max_length=100, null=True)),
                ('button_text_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('button_text_de', models.CharField(blank=True, max_length=100, null=True)),
                ('button_text_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('button_link', models.CharField(blank=True, help_text="\n                If it is a link to an external page, please start with http:// or https://.\n                If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.\n            ", max_length=500, null=True, validators=[core.validators.button_link_validator])),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
    ]
