# Generated by Django 4.0.2 on 2022-03-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='job_description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='job_description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='job_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='job_description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_ar',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_de',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='name_fr',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='review_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='review_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='review_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='review_fr',
            field=models.TextField(null=True),
        ),
    ]
