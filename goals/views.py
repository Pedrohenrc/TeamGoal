from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Goal
from teams.models import Team
class GoalCreateView(CreateView, LoginRequiredMixin):
    model = Goal
    template_name = "goals/goal_form.html"
    fields = ['title', 'description', 'deadline', 'status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs.get('team_id')

        print(f"DEBUG: team_id = {team_id}")

        if team_id:
            try:
                team = Team.objects.get(pk=team_id)

                if self.request.user in team.members.all() or self.request.user == team.owner:
                    context['team'] = team
                    context['selected_team_id'] = team_id
            except Team.DoesNotExist:
                pass
        else:
            context['user_teams'] = self.request.user.teams.all()

        return context
    def form_valid(self, form):
        team_id = self.kwargs.get('team_id')

        if team_id:
            try:
                team = Team.objects.get(pk=team_id)
                if self.request.user in team.members.all() or self.request.user == team.owner:
                    form.instance.team = team
                else:
                    return self.form_invalid(form)
            except Team.DoesNotExist:
                return self.form_invalid
        else:
            team_id_from_post = self.request.POST.get('team')
            if team_id_from_post:
                try:
                    team = Team.objects.get(pk=team_id_from_post)
                    if self.request.user in team.members.all() or self.request.user == team.owner:
                        form.instance.team = team
                    else:
                        return self.form_invalid(form)
                except Team.DoesNotExist:
                    return self.form_invalid(form)
            else:
                return self.form_invalid(form)
        return super().form_valid(form)
        
    def get_success_url(self):
        team_id = self.kwargs.get('team_id')
        if team_id:
            return reverse_lazy('team-detail', kwargs={'pk': team_id})
        return reverse_lazy('goal-list')
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

        for goal in queryset:
            completed = goal.subtasks.filter(is_completed=True).count()
            total = goal.subtasks.count()
            goal.progress_display = f"{completed} de {total}"
            goal.completed_count = completed
            goal.total_count = total
            
            
         
        context['pending_count'] = queryset.filter(status='pending').count()
        context['in_progress_count'] = queryset.filter(status='in_progress').count()
        context['completed_count'] = queryset.filter(status='completed').count()
            
        return context

class GoalDetailView (DetailView, LoginRequiredMixin):
    model = Goal
    context_object_name = "goal"
    template_name = "goals/goal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goal = self.object

        subtasks = goal.subtasks.all()
        completed_count = subtasks.filter(is_completed=True).count()
        total_count = subtasks.count()

        context['subtasks_completed'] = completed_count
        context['subtasks_total'] = total_count

        return context
class GoalUpdateView (UpdateView, LoginRequiredMixin):
    model = Goal
    fields = ['title', 'description', 'deadline', 'status']
    template_name = "goals/goal_form.html"
    success_url = reverse_lazy("goal-list")
    
