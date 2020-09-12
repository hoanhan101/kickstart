from django.urls import path

from . import views

app_name = "goals"
urlpatterns = [
    path('', views.GoalListView.as_view(), name='goal_list'),
    path("goal/<int:id>/", views.GoalDetailView.as_view(), name="goal_detail"),
    path("goal/create/", views.GoalCreateView.as_view(), name="goal_create"),
]
