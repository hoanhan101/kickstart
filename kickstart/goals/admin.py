from django.contrib import admin

from .models import Goal, System, Progress


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_completed', 'pain_level')

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('goal', 'name', 'measurable_data', 'measurable_unit', 'measurable_context')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('system', 'date', 'is_completed', 'measurable_data', 'measurable_context')
