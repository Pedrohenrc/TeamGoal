from django.urls import path
from .views import HomeView, DashboardView, GoogleLoginView, GitHubLoginView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('login/github/', GitHubLoginView.as_view(), name='github_login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]