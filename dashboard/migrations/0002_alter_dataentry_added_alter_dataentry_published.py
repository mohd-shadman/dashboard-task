# Generated by Django 5.0.6 on 2024-07-26 17:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataentry',
            name='added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
