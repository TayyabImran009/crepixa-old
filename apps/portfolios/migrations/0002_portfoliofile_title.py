# Generated by Django 4.0.2 on 2022-04-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliofile',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
