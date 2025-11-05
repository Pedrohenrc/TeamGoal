from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team
from .forms import TeamForm
# Create your views here.

class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return self.request.user.teams.all()
    
class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "teams/team_detail.html"
    context_object_name = "team"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.object
        
        for goal in team.goals.all():
            completed = goal.subtasks.filter(is_completed=True).count()
            total = goal.subtasks.count()
            goal.progress_display = f"{completed} de {total}"
            goal.completed_count = completed
            goal.total_count = total
        
        return context

class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = "teams/team_form.html"
    success_url = reverse_lazy("team-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        form.instance.members.add(self.request.user)
        return response
    
class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = "teams/team_form.html"
    success_url = reverse_lazy("team-list")

class TeamDeleteView(DeleteView, LoginRequiredMixin):
    model = Team
    success_url = reverse_lazy("team-list")
