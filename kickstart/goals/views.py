from django.shortcuts import render
from django.http import HttpResponse, Http404

from . import models


def goal_list(request):
    user = request.user
    if user.is_authenticated:
        payload = []

        goals = models.Goal.objects.filter(user=user)
        for goal in goals:
            systems = models.System.objects.filter(goal=goal)

            sys = []
            for system in systems:
                progress = models.Progress.objects.filter(system=system)
                sys.append({
                    'system': system,
                    'progress': progress
                })

            payload.append({
                'goal': goal,
                'systems': sys
            })

        return render(request, 'goals/goal_list.html', {'payload': payload})
    return render(request, '404.html')
