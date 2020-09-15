from datetime import date
from django.conf import settings
from django.db import models


class Goal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_of',
        verbose_name='Created by',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='What do you want to achieve?',
    )
    pain_level = models.TextField(
        null=True,
        blank=True,
        verbose_name='What kind of pain do you want?',
        help_text='The real challenge is not determining if you want the result, but if you are willing to accept the sacrifices required to achieve your goal. It is easy to sit around and think what we could do or what we would like to do. It is an entirely different thing to accept the tradeoffs that come with our goals. Everybody wants a gold medal. Few people want to train like an Olympian.', # noqa
    )
    is_completed = models.BooleanField(
        blank=True,
        default=False,
    )

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    def __str__(self):
        return f'{self.name}'


class System(models.Model):
    CHILI = '#C21807'
    RUBY = '#E0115F'
    MULBERRY = '#C64B8C'
    LILAC = '#B66OCD'
    PUNCH = '#EC5578'
    FRENCH_ROSE = '#F64A8A'
    LOLLIPOP = '#81007F'
    PLUM = '#8D4585'
    TAFFY = '#F987C5'
    TIGER = '#FD6A02'
    BUMBLEBEE = '#FCE205'
    HONEY = '#EB9605'
    LEMON = '#EFFD5F'
    MINT = '#98FB98'
    SEA = '#2E8B57'
    FERN = '#4F7942'
    JUNGLE = '#29AB87'
    LAVA = '#808588'
    STEEL = '#4682B4'
    AZURE = '#0080FE'
    CAROLINA = '#57A0D2'

    COLOR_CHOICES = [
        (CHILI, 'Chili'),
        (RUBY, 'Ruby'),
        (MULBERRY, 'Mulberry'),
        (LILAC, 'Lilac'),
        (PUNCH, 'Punch'),
        (FRENCH_ROSE, 'French Rose'),
        (LOLLIPOP, 'Lollipop'),
        (PLUM, 'Plum'),
        (TAFFY, 'Taffy'),
        (TIGER, 'Tiger'),
        (BUMBLEBEE, 'Bumblelee'),
        (HONEY, 'Honey'),
        (LEMON, 'Lemon'),
        (MINT, 'Mint'),
        (SEA, 'Sea'),
        (FERN, 'Fern'),
        (JUNGLE, 'Jungle'),
        (LAVA, 'Lava'),
        (STEEL, 'Steel'),
        (AZURE, 'Azure'),
        (CAROLINA, 'Carolina'),
    ]

    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name='goal_of',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='What is your system?',
        help_text='If you’re a writer, your goal is to write a book. Your system is the writing schedule that you follow each week. If you’re a runner, your goal is to run a marathon. Your system is your training schedule for the month.', # noqa
    )
    color = models.CharField(
        max_length=7,
        choices=COLOR_CHOICES,
        default=HONEY,
        verbose_name='What color do you want?',
        help_text='Use color to help you see your progress on the calendar and chart better.',
    )
    measurable_data = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='What is the minimum threshold you want to hit?',
        help_text='You want to push hard enough to make progress, but not so much that it is unsustainable. For example, I want to lose at least 5 pounds this month or I want to write at least 500 words today.', # noqa
    )
    measurable_unit = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='What is its unit?',
        help_text='The unit can be anything: reps, pounds, sales, words, and so on. You name it.', # noqa
    )
    measurable_context = models.TextField(
        null=True,
        blank=True,
        verbose_name='Anything else you want to remind yourself?',
        help_text='What are the things that you want to avoid at all cost until you have succeeded? Do you have a specific plan for when, where, and how you will perform the behavior?', # noqa
    )

    class Meta:
        verbose_name = 'System'
        verbose_name_plural = 'Systems'

    def __str__(self):
        return f'{self.name}'


class Progress(models.Model):
    system = models.ForeignKey(
        System,
        on_delete=models.CASCADE,
        related_name='system_of',
    )
    date = models.DateField(
        default=date.today,
        verbose_name='What is your check-in date?',
    )
    is_completed = models.BooleanField(
        default=True,
        verbose_name='Did you complete it?',
    )
    measurable_data = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='What was the actual number?',
    )
    measurable_context = models.TextField(
        null=True,
        blank=True,
        verbose_name='Anything else you want to reflect?',
        help_text='What was a highlight today? Was there anything challenging? What are you looking forward to? What needs growth and nurturing?', # noqa
    )

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'

    def __str__(self):
        return f'{self.date}'
