# Generated by Django 4.0.2 on 2022-03-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street_house_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
