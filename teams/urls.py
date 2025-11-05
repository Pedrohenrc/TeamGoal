from django.urls import path
from .views import TeamListView, TeamDetailView, TeamCreateView, TeamUpdateView, TeamDeleteView, TeamJoinByCodeView, accept_join_request, reject_join_request

urlpatterns = [
    path("", TeamListView.as_view(), name="team-list"),
    path("create/", TeamCreateView.as_view(), name="team-create"),
    path("<int:pk>/", TeamDetailView.as_view(), name="team-detail"),
    path("<int:pk>/edit/", TeamUpdateView.as_view(), name="team-edit"),
    path("<int:pk>/delete/", TeamDeleteView.as_view(), name="team-delete"),
    path('join/', TeamJoinByCodeView.as_view(), name='team-join-code'),
    path('requests/<int:request_id>/accept/', accept_join_request, name='accept-join-request'),
    path('requests/<int:request_id>/reject/', reject_join_request, name='reject-join-request'),
    ]