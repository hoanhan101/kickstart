# Generated by Django 3.0.10 on 2020-09-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_auto_20200912_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='progress',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
