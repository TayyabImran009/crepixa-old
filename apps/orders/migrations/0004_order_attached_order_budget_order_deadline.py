# Generated by Django 4.0.2 on 2022-05-30 02:50

import core.utils.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_managers_remove_order_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='attached',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.utils.get_file_path),
        ),
        migrations.AddField(
            model_name='order',
            name='budget',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
