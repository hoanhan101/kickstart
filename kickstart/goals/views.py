from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic


from . import models


class GoalListView(LoginRequiredMixin, generic.View):

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


class GoalDetailView(LoginRequiredMixin, generic.DetailView):

    model = models.Goal
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'goals/goal_detail.html'


class GoalCreateView(LoginRequiredMixin, generic.CreateView):

    model = models.Goal
    fields = ['name', 'pain_level']
    template_name = 'goals/goal_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, 'Created successfully'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('goals:goal_list')


class GoalUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = models.Goal
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ['name', 'pain_level', 'is_completed']
    template_name = 'goals/goal_update.html'

    def get_success_url(self):
        return reverse('goals:goal_detail', kwargs=self.kwargs)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Updated successfully'
        )
        return super().form_valid(form)


class GoalDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = models.Goal
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = 'goals/goal_delete.html'

    def get_success_url(self):
        return reverse('goals:goal_list')
