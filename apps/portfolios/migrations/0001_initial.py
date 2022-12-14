# Generated by Django 4.0.2 on 2022-04-14 04:20

import core.utils.utils
import core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('name_en', models.CharField(max_length=500, null=True, unique=True)),
                ('name_ar', models.CharField(max_length=500, null=True, unique=True)),
                ('name_de', models.CharField(max_length=500, null=True, unique=True)),
                ('name_fr', models.CharField(max_length=500, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('thumbnail', models.ImageField(upload_to=core.utils.utils.get_file_path)),
                ('project_date', models.DateField(null=True)),
                ('url_slug', models.CharField(max_length=500, unique=True)),
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
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ar', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('description_fr', models.TextField(null=True)),
                ('categories', models.ManyToManyField(to='portfolios.Category')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioHomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('image', models.ImageField(upload_to=core.utils.utils.get_file_path)),
            ],
            options={
                'verbose_name': 'Portfolio(Homepage)',
                'verbose_name_plural': 'Portfolios(Homepage)',
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('button_text', models.CharField(max_length=100)),
                ('button_text_en', models.CharField(max_length=100, null=True)),
                ('button_text_ar', models.CharField(max_length=100, null=True)),
                ('button_text_de', models.CharField(max_length=100, null=True)),
                ('button_text_fr', models.CharField(max_length=100, null=True)),
                ('button_link', models.CharField(help_text="\n            If it is a link to an external page, please start with http:// or https://.\n            If it is a link to a page on this website, please start with / right after domain and DON'T INCLUDE language.\n        ", max_length=500, validators=[core.validators.button_link_validator])),
                ('bg_image', models.ImageField(upload_to=core.utils.utils.get_file_path)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('name', models.CharField(max_length=500)),
                ('name_en', models.CharField(max_length=500, null=True)),
                ('name_ar', models.CharField(max_length=500, null=True)),
                ('name_de', models.CharField(max_length=500, null=True)),
                ('name_fr', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Sub categories',
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('name_en', models.CharField(max_length=500, null=True, unique=True)),
                ('name_ar', models.CharField(max_length=500, null=True, unique=True)),
                ('name_de', models.CharField(max_length=500, null=True, unique=True)),
                ('name_fr', models.CharField(max_length=500, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending')),
                ('portfolio_file', models.FileField(upload_to=core.utils.utils.get_file_path)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='sub_categories',
            field=models.ManyToManyField(to='portfolios.SubCategory'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='tags',
            field=models.ManyToManyField(to='portfolios.Tag'),
        ),
    ]
