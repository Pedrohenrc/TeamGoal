from django.urls import path
from .views import ContributionCreateView, ContributionDetailView, ContributionDeleteView, ContributionListView, ContributionUpdateView

urlpatterns = [
    path("", ContributionListView.as_view(), name="contribution-list"),
    path("<int:pk>/", ContributionDetailView.as_view(), name="contribution-detail"),
    path("<int:pk>/editar", ContributionUpdateView.as_view(), name="contribution-update"),
    path("create/", ContributionCreateView.as_view(), name="contribution-create"),
    path("<int:pk>/delete", ContributionDeleteView.as_view(), name="contribution-delete")
]