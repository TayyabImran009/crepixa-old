# Generated by Django 4.0.2 on 2022-04-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_slug',
            field=models.CharField(default='a', max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='url_slug_ar',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_slug_de',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_slug_en',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url_slug_fr',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]