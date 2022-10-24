# Generated by Django 4.0.2 on 2022-03-13 10:19

import core.utils.utils
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('ordering_number', models.IntegerField(help_text='Ascending ordering.')),
                ('logo', models.ImageField(upload_to=core.utils.utils.get_file_path)),
                ('name', models.CharField(max_length=500)),
                ('job_description', models.TextField()),
                ('review', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('pobs', django.db.models.manager.Manager()),
            ],
        ),
    ]