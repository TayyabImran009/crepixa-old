# Generated by Django 4.0.2 on 2022-04-02 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_serviceordersection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='socialmediapage',
            name='icon',
        ),
        migrations.AddField(
            model_name='socialmediapage',
            name='fa_css_class',
            field=models.CharField(choices=[], default='fa', max_length=100),
            preserve_default=False,
        ),
    ]
