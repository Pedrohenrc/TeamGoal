"""
URL configuration for TeamGoal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from teams.api.views import TeamViewSet
from goals.api.views import GoalViewSet
from subgoals.api.views import SubGoalViewSet
from contributions.api.views import ContributionViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'subgoals', SubGoalViewSet, basename='subgoal')
router.register(r'contributions', ContributionViewSet, basename='contribution')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include(router.urls)),
        path('auth/', include('dj_rest_auth.urls')),
    ])),
    path('', include("core.urls")),
    path('team/', include("teams.urls")),
    path('goals/', include("goals.urls")),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
