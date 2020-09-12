from django.shortcuts import render
from django.views.generic import View, DetailView


from . import models


class GoalListView(View):

    def get(self, request):
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


class GoalDetailView(DetailView):

    model = models.Goal
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'goals/goal_detail.html'
