from django.urls import path

from . import views

app_name = "goals"
urlpatterns = [
    path('', views.GoalListView.as_view(), name='goal_list'),
    path('goal/<int:id>/', views.GoalDetailView.as_view(), name="goal_detail"),
    path('goal/create/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goal/update/<int:id>/', views.GoalUpdateView.as_view(), name='goal_update'),
    path('goal/delete/<int:id>/', views.GoalDeleteView.as_view(), name='goal_delete'),

    path('system/<int:id>/', views.SystemDetailView.as_view(), name='system_detail'),
    path('system/create/', views.SystemCreateView.as_view(), name='system_create'),
    path('system/update/<int:id>/', views.SystemUpdateView.as_view(), name='system_update'),
    path('system/delete/<int:id>/', views.SystemDeleteView.as_view(), name='system_delete'),

    path('progress/<int:id>/', views.ProgressDetailView.as_view(), name='progress_detail'),
    path('progress/create/', views.ProgressCreateView.as_view(), name='progress_create'),
    path('progress/update/<int:id>/', views.ProgressUpdateView.as_view(), name='progress_update'),
    path('progress/delete/<int:id>/', views.ProgressDeleteView.as_view(), name='progress_delete'),
]
