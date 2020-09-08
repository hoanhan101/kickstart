from django.shortcuts import render
from django.http import HttpResponse, Http404

from . import models


def goal_list(request):
    user = request.user
    if user.is_authenticated:
        goals = models.Goal.objects.filter(user=user)
        context = {
            'goals': goals
        }
        return render(request, 'goals/goal_list.html', context)
    return render(request, '404.html')
