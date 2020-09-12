from django.conf import settings
from django.db import models


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_of')
    name = models.CharField(max_length=200)
    pain_level = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(blank=True, default=False)

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
    SPACE = '#1C2951'
    COFFEE = '#4B3619'
    ESPRESSO = '#4B382A'

    COLOR_CHOICES = [
        (CHILI, 'Chili'),
        (RUBY, 'Ruby'),
        (MULBERRY, 'Mulberry'),
        (LILAC, 'Lilac'),
        (PUNCH, 'PUNCH'),
        (FRENCH_ROSE, 'French Rose'),
        (LOLLIPOP, 'Lollipop'),
        (PLUM, 'Plum'),
        (TAFFY, 'Taffy'),
        (TIGER, 'Tiger'),
        (BUMBLEBEE, 'Bumblelee'),
        (HONEY, 'Honey'),
        (LEMON, 'Lemon'),
        (MINT, 'Mint'),
        (MINT, 'Mint'),
        (SEA, 'Sea'),
        (FERN, 'Fern'),
        (JUNGLE, 'Jungle'),
        (LAVA, 'Lava'),
        (STEEL, 'Steel'),
        (AZURE, 'Azure'),
        (CAROLINA, 'Carolina'),
        (SPACE, 'Space'),
        (COFFEE, 'Coffee'),
        (ESPRESSO, 'Espresso'),
    ]

    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='goal_of')
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default=HONEY)
    measurable_data = models.PositiveIntegerField(null=True, blank=True)
    measurable_unit = models.CharField(max_length=200, null=True, blank=True)
    measurable_context = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'System'
        verbose_name_plural = 'Systems'

    def __str__(self):
        return f'{self.name}'


class Progress(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='system_of')
    date = models.DateField()
    is_completed = models.BooleanField(default=True)
    measurable_data = models.PositiveIntegerField(null=True, blank=True)
    measurable_context = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'

    def __str__(self):
        return f'{self.date}'
