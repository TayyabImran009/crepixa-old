# Generated by Django 4.0.2 on 2022-04-17 16:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_options_alter_service_icon'),
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
    ]