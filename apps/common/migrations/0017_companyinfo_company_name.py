# Generated by Django 4.0.2 on 2022-05-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_alter_aboutussection_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='company_name',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
