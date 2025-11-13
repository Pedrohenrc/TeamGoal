from django.urls import path, include
from .views import SubgoalCreateView, SubgoalUpdateView, SubgoalDetailView, SubgoalDeleteView, SubgoalListView, complete_subtask

urlpatterns = [
    path("", SubgoalListView.as_view(), name="subgoal-list"),
    path("create/", SubgoalCreateView.as_view(), name="subgoal-create"),
    path("<int:subgoal_id>", SubgoalDetailView.as_view(), name="subgoal-detail"),
    path("<int:subgoal_id>/editar", SubgoalUpdateView.as_view(), name="subgoal-update"),
    path("<int:subgoal_id>/deletar", SubgoalDeleteView.as_view(), name="subgoal-delete" ),
    path("<int:subgoal_id>/contributions", include("contributions.urls")),
    path('<int:pk>/toggle-complete/', complete_subtask, name='subgoal-toggle-complete'),

]