from django.urls import path

from kickstart.users.views import (
    UserRedirectView,
    UserUpdateView,
    UserDetailView,
)

app_name = "users"
urlpatterns = [
    path("redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=UserDetailView.as_view(), name="detail"),
]
