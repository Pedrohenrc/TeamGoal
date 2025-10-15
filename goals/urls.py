from django.urls import path, include
from .views import GoalCreateView, GoalDetailView, GoalListView, GoalUpdateView

urlpatterns = [
    path("", GoalListView.as_view(), name="goal-list"),
    path("create/", GoalCreateView.as_view(), name="goal-create"),
    path("create/<int:team_id>/", GoalCreateView.as_view(), name="goal-create-for-team"),
    path("<int:pk>", GoalDetailView.as_view(), name='goal-detail'),
    path("<int:pk>/editar/", GoalUpdateView.as_view(), name='goal-update'),
    path("<int:goal_id>/subtasks/", include("subgoals.urls")),
    path("<int:goal_id>/contributions/", include("contributions.urls")),
]
