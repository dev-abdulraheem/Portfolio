# Generated by Django 3.2.16 on 2023-01-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0012_remove_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]
