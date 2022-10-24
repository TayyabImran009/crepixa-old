# Generated by Django 4.0.2 on 2022-03-13 15:21

import core.utils.utils
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=core.utils.utils.get_file_path)),
                ('city_country', models.CharField(help_text='Berlin, Germany', max_length=500)),
                ('city_country_en', models.CharField(help_text='Berlin, Germany', max_length=500, null=True)),
                ('city_country_ar', models.CharField(help_text='Berlin, Germany', max_length=500, null=True)),
                ('city_country_de', models.CharField(help_text='Berlin, Germany', max_length=500, null=True)),
                ('city_country_fr', models.CharField(help_text='Berlin, Germany', max_length=500, null=True)),
                ('address', models.CharField(max_length=500)),
                ('address_en', models.CharField(max_length=500, null=True)),
                ('address_ar', models.CharField(max_length=500, null=True)),
                ('address_de', models.CharField(max_length=500, null=True)),
                ('address_fr', models.CharField(max_length=500, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_number_en', models.CharField(max_length=20, null=True)),
                ('phone_number_ar', models.CharField(max_length=20, null=True)),
                ('phone_number_de', models.CharField(max_length=20, null=True)),
                ('phone_number_fr', models.CharField(max_length=20, null=True)),
                ('email_address', models.CharField(max_length=100)),
                ('email_address_en', models.CharField(max_length=100, null=True)),
                ('email_address_ar', models.CharField(max_length=100, null=True)),
                ('email_address_de', models.CharField(max_length=100, null=True)),
                ('email_address_fr', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('title_en', models.CharField(max_length=500, null=True)),
                ('title_ar', models.CharField(max_length=500, null=True)),
                ('title_de', models.CharField(max_length=500, null=True)),
                ('title_fr', models.CharField(max_length=500, null=True)),
                ('subtitle', models.TextField()),
                ('subtitle_en', models.TextField(null=True)),
                ('subtitle_ar', models.TextField(null=True)),
                ('subtitle_de', models.TextField(null=True)),
                ('subtitle_fr', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('text', models.CharField(max_length=500)),
                ('text_en', models.CharField(max_length=500, null=True)),
                ('text_ar', models.CharField(max_length=500, null=True)),
                ('text_de', models.CharField(max_length=500, null=True)),
                ('text_fr', models.CharField(max_length=500, null=True)),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('icon', models.ImageField(upload_to=core.utils.utils.get_file_path)),
                ('link', models.URLField()),
                ('name', models.CharField(max_length=500)),
                ('name_en', models.CharField(max_length=500, null=True)),
                ('name_ar', models.CharField(max_length=500, null=True)),
                ('name_de', models.CharField(max_length=500, null=True)),
                ('name_fr', models.CharField(max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='ordering_number',
            field=models.IntegerField(help_text='Ascending'),
        ),
    ]
