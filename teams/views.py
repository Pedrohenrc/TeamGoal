from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team
from .forms import TeamForm
# Create your views here.

class TeamListView(LoginRequiredMixin, ListView):
    Model = Team
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return self.request.user.teams.all()
    
class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "teams/team_detail.html"
    context_object_name = "team"

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