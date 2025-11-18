from django.urls import path
from .views import ContributionDetailView, ContributionDeleteView, ContributionListView, ContributionUpdateView

urlpatterns = [
    path("", ContributionListView.as_view(), name="contribution-list"),
    path("<uuid:pk>/", ContributionDetailView.as_view(), name="contribution-detail"),
    path("<uuid:pk>/editar", ContributionUpdateView.as_view(), name="contribution-update"),
    path("<uuid:pk>/delete", ContributionDeleteView.as_view(), name="contribution-delete")
]