# Generated by Django 4.0.2 on 2022-04-05 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_city_user_company_name_user_street_house_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
