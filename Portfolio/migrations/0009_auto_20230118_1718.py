# Generated by Django 3.2.16 on 2023-01-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0008_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
