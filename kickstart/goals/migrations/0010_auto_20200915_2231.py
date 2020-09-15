# Generated by Django 3.0.10 on 2020-09-15 22:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0009_auto_20200915_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='name',
            field=models.CharField(max_length=200, verbose_name='What do you want to achieve?'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='pain_level',
            field=models.TextField(blank=True, help_text='The real challenge is not determining if you want the result, but if you are willing to accept the sacrifices required to achieve your goal. It is easy to sit around and think what we could do or what we would like to do. It is an entirely different thing to accept the tradeoffs that come with our goals. Everybody wants a gold medal. Few people want to train like an Olympian.', null=True, verbose_name='What kind of pain do you want?'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='What is your check-in date?'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='is_completed',
            field=models.BooleanField(default=True, verbose_name='Did you complete it?'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='measurable_context',
            field=models.TextField(blank=True, help_text='What was a highlight today? Was there anything challenging? What are you looking forward to? What needs growth and nurturing?', null=True, verbose_name='Anything else you want to reflect?'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='measurable_data',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='What was the actual number?'),
        ),
        migrations.AlterField(
            model_name='system',
            name='color',
            field=models.CharField(choices=[('#C21807', 'Chili'), ('#E0115F', 'Ruby'), ('#C64B8C', 'Mulberry'), ('#B66OCD', 'Lilac'), ('#EC5578', 'Punch'), ('#F64A8A', 'French Rose'), ('#81007F', 'Lollipop'), ('#8D4585', 'Plum'), ('#F987C5', 'Taffy'), ('#FD6A02', 'Tiger'), ('#FCE205', 'Bumblelee'), ('#EB9605', 'Honey'), ('#EFFD5F', 'Lemon'), ('#98FB98', 'Mint'), ('#2E8B57', 'Sea'), ('#4F7942', 'Fern'), ('#29AB87', 'Jungle'), ('#808588', 'Lava'), ('#4682B4', 'Steel'), ('#0080FE', 'Azure'), ('#57A0D2', 'Carolina')], default='#EB9605', help_text='Use color to help you see your progress on the calendar and chart better.', max_length=7, verbose_name='What color do you want?'),
        ),
        migrations.AlterField(
            model_name='system',
            name='measurable_context',
            field=models.TextField(blank=True, help_text='What are the things that you want to avoid at all cost until you have succeeded? Do you have a specific plan for when, where, and how you will perform the behavior?', null=True, verbose_name='Anything else you want to remind yourself?'),
        ),
        migrations.AlterField(
            model_name='system',
            name='measurable_data',
            field=models.PositiveIntegerField(blank=True, help_text='You want to push hard enough to make progress, but not so much that it is unsustainable. For example, I want to lose at least 5 pounds this month or I want to write at least 500 words today.', null=True, verbose_name='What is the minimum threshold you want to hit?'),
        ),
        migrations.AlterField(
            model_name='system',
            name='measurable_unit',
            field=models.CharField(blank=True, help_text='The unit can be anything: reps, pounds, sales, words, and so on. You name it.', max_length=200, null=True, verbose_name='What is its unit?'),
        ),
        migrations.AlterField(
            model_name='system',
            name='name',
            field=models.CharField(help_text='If you’re a writer, your goal is to write a book. Your system is the writing schedule that you follow each week. If you’re a runner, your goal is to run a marathon. Your system is your training schedule for the month.', max_length=200, verbose_name='What is your system?'),
        ),
    ]