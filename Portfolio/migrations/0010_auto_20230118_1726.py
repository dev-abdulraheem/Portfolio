# Generated by Django 3.2.16 on 2023-01-18 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0009_auto_20230118_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='start_date',
        ),
    ]
