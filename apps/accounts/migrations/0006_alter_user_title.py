# Generated by Django 4.0.2 on 2022-06-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(choices=[('mr', 'Mr.'), ('ms', 'Ms.'), ('div', 'Div.')], max_length=3),
        ),
    ]
