from django.urls import path, include
from .views import GoalCreateView, GoalDetailView, GoalListView, GoalUpdateView, GoalDeleteView

urlpatterns = [
    path("", GoalListView.as_view(), name="goal-list"),
    path("create/", GoalCreateView.as_view(), name="goal-create"),
    path("create/<uuid:team_id>/", GoalCreateView.as_view(), name="goal-create-for-team"),
    path("<uuid:pk>", GoalDetailView.as_view(), name='goal-detail'),
    path("<uuid:pk>/editar/", GoalUpdateView.as_view(), name='goal-update'),
    path("<uuid:pk>/deletar/", GoalDeleteView.as_view(), name='goal-delete'),
    path("<uuid:goal_id>/subtasks/", include("subgoals.urls")),
    path("<uuid:goal_id>/contributions/", include("contributions.urls")),
]
