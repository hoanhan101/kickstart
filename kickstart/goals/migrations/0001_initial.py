# Generated by Django 3.0.10 on 2020-09-09 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_completed', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Goal',
                'verbose_name_plural': 'Goals',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('measurable_data', models.PositiveIntegerField(blank=True, null=True)),
                ('measurable_unit', models.CharField(blank=True, max_length=200, null=True)),
                ('measurable_context', models.TextField(blank=True, null=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_of', to='goals.Goal')),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_completed', models.BooleanField()),
                ('measurable_data', models.PositiveIntegerField(blank=True, null=True)),
                ('measurable_context', models.TextField(blank=True, null=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='system_of', to='goals.System')),
            ],
            options={
                'verbose_name': 'Progress',
                'verbose_name_plural': 'Progress',
            },
        ),
    ]
