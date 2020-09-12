from django.urls import path

from . import views

app_name = "goals"
urlpatterns = [
    path('', views.GoalListView.as_view() , name='goal_list'),
    path("<int:id>/", views.GoalDetailView.as_view(), name="goal_detail"),
]
