# Generated by Django 3.0.10 on 2020-09-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_system_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='color',
            field=models.CharField(choices=[('red', '#ee2324'), ('orange', '#ec6225'), ('yellow', '#f3bf0f'), ('green', '#00a14f'), ('blue', '#4b7cbe')], default='orange', max_length=7),
        ),
    ]
