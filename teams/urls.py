from django.urls import path
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamUpdateView

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),
    path("create/", TeamCreateView.as_view(), name="team-create"),
    path("<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("<int:pk>/edit/", TeamUpdateView.as_view(), name="team-edit"),
]