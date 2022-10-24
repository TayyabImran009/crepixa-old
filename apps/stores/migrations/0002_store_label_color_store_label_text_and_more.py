# Generated by Django 4.0.2 on 2022-04-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='label_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('red', 'Red')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='label_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='label_text_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='label_text_de',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='label_text_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='label_text_fr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
