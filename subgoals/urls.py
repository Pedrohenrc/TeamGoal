from django.urls import path, include
from .views import SubgoalCreateView, SubgoalUpdateView, SubgoalDetailView, SubgoalDeleteView, SubgoalListView, complete_subtask

urlpatterns = [
    path("", SubgoalListView.as_view(), name="subgoal-list"),
    path("create/", SubgoalCreateView.as_view(), name="subgoal-create"),
    path("<uuid:subgoal_id>", SubgoalDetailView.as_view(), name="subgoal-detail"),
    path("<uuid:subgoal_id>/editar", SubgoalUpdateView.as_view(), name="subgoal-update"),
    path("<uuid:subgoal_id>/deletar", SubgoalDeleteView.as_view(), name="subgoal-delete" ),
    path("<uuid:subgoal_id>/contributions", include("contributions.urls")),
    path('<uuid:pk>/toggle-complete/', complete_subtask, name='subgoal-toggle-complete'),

]