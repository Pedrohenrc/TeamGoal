from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Goal
class GoalCreateView(CreateView, LoginRequiredMixin):
    model = Goal
    fields = ['title', 'description', 'deadline', 'status']
    template_name = "goals/goal_form.html"
    success_url = reverse_lazy("goal-list")

class GoalListView(ListView, LoginRequiredMixin):
    model = Goal
    context_object_name = "goals"
    template_name = "goals/goal_list.html"

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
            
         
        context['pending_count'] = queryset.filter(status='pending').count()
        context['in_progress_count'] = queryset.filter(status='in_progress').count()
        context['completed_count'] = queryset.filter(status='completed').count()
            
        return context

class GoalDetailView (DetailView, LoginRequiredMixin):
        model = Goal
        context_object_name = "goal"
        template_name = "goals/goal_detail.html"

class GoalUpdateView (UpdateView, LoginRequiredMixin):
     model = Goal
     fields = ['title', 'description', 'deadline', 'status']
     template_name = "goals/goal_form.html"
     success_url = reverse_lazy("goat-list")
    
