# Generated by Django 3.0.10 on 2020-09-09 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='pain_level',
            field=models.TextField(blank=True, null=True),
        ),
    ]
