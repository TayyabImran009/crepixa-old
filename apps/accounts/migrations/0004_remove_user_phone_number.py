# Generated by Django 4.0.2 on 2022-04-08 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
