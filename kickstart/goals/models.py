from django.conf import settings
from django.db import models


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_of')
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField()
    pain_level = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'

    def __str__(self):
        return f'{self.name}'


class System(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='goal_of')
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=6, null=True, blank=True)
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
    is_completed = models.BooleanField()
    measurable_data = models.PositiveIntegerField(null=True, blank=True)
    measurable_context = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'

    def __str__(self):
        return f'{self.date}'
