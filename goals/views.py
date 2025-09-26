from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Goal
class GoalCreateView(CreateView, LoginRequiredMixin):
    Model = Goal
    fields = ['title', 'description', 'deadline', 'status']
    success_url = reverse_lazy("goal-list")

class GoalListView(ListView, LoginRequiredMixin):
    Model = Goal
    context_object_name = "goals"

    def get_queryset(self):
        queryset = Goal.objects.all()

        status_param = self.request.GET.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)

        team_param = self.request.GET.get("team")
        if team_param:
            queryset = queryset.filter(team__id=team_param)

        user_param = self.request.GET.get("user")
        if user_param:
            queryset = queryset.filter(contributions__user__id=user_param)

        return queryset

class GoalDetailView (DetailView, LoginRequiredMixin):
        model = Goal
        context_object_name = "goal"

class GoalUpdateView (UpdateView, LoginRequiredMixin):
     model = Goal
     fields = ['title', 'description', 'deadline', 'status']
     success_url = reverse_lazy("goat-list")