from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django import forms

from .models import Goal, System, Progress


class GoalListView(LoginRequiredMixin, generic.View):

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            payload = []

            goals = Goal.objects.filter(user=user)
            for goal in goals:
                systems = System.objects.filter(goal=goal)

                sys = []
                for system in systems:
                    progress = Progress.objects.filter(system=system)
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

    model = Goal
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/goal_detail.html'


class GoalCreateView(LoginRequiredMixin, generic.CreateView):

    model = Goal
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

    model = Goal
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

    model = Goal
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/goal_delete.html'

    def get_success_url(self):
        return reverse('goals:goal_list')


class SystemDetailView(LoginRequiredMixin, generic.DetailView):

    model = System
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/system_detail.html'


class SystemCreateView(LoginRequiredMixin, generic.CreateView):

    model = System
    fields = ['goal', 'name', 'color', 'measurable_data', 'measurable_unit', 'measurable_context']
    template_name = 'goals/system_create.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['goal'].queryset = Goal.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Created successfully'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('goals:goal_list')


class SystemUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = System
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ['name', 'color', 'measurable_data', 'measurable_unit', 'measurable_context']
    template_name = 'goals/system_update.html'

    def get_success_url(self):
        return reverse('goals:system_detail', kwargs=self.kwargs)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Updated successfully'
        )
        return super().form_valid(form)


class SystemDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = System
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/system_delete.html'

    def get_success_url(self):
        return reverse('goals:goal_list')


class ProgressDetailView(LoginRequiredMixin, generic.DetailView):

    model = Progress
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/progress_detail.html'


class ProgressCreateView(LoginRequiredMixin, generic.CreateView):

    model = Progress
    fields = ['system', 'date', 'is_completed', 'measurable_data', 'measurable_context']
    template_name = 'goals/progress_create.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['system'].queryset = System.objects.filter(goal__user=self.request.user)
        form.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Created successfully'
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('goals:goal_list')


class ProgressUpdateView(LoginRequiredMixin, generic.UpdateView):

    model = Progress
    slug_field = 'id'
    slug_url_kwarg = 'id'
    fields = ['date', 'is_completed', 'measurable_data', 'measurable_context']
    template_name = 'goals/progress_update.html'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['date'].widget = forms.widgets.DateInput(attrs={'type': 'date'})
        return form

    def get_success_url(self):
        return reverse('goals:progress_detail', kwargs=self.kwargs)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Updated successfully'
        )
        return super().form_valid(form)


class ProgressDeleteView(LoginRequiredMixin, generic.DeleteView):

    model = Progress
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'goals/progress_delete.html'

    def get_success_url(self):
        return reverse('goals:goal_list')
