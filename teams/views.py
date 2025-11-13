from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team, TeamJoinRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
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

class TeamJoinByCodeView(LoginRequiredMixin, CreateView):
    model = TeamJoinRequest
    fields = []
    template_name = "teams/team_join_code.html"

    def post(self, request, *args, **kwargs):
        code = request.POST.get('code', '').upper()
        
        try:
            team = Team.objects.get(code=code)
        except Team.DoesNotExist:
            return redirect('team-join-code')
        
        if request.user in team.members.all():
            return redirect('team-detail', pk=team.pk)
        
        existing = TeamJoinRequest.objects.filter(team=team, user=request.user).first()
        if existing:
            if existing.status == 'pending':
                return render(request, self.template_name, {'error': 'Você já solicitou acesso'})
            else:
                existing.delete()
        
        TeamJoinRequest.objects.create(team=team, user=request.user)
        return render(request, self.template_name, {'success': 'Pedido enviado com sucesso!'})

        
def accept_join_request(request, request_id):
        join_req = get_object_or_404(TeamJoinRequest, id=request_id)
        team = join_req.team
        
        if request.user != team.owner:
            return redirect('team-list')
        
        join_req.status = 'accepted'
        join_req.save()
        team.members.add(join_req.user)
        
        return redirect('team-detail', pk=team.pk)

def reject_join_request(request, request_id):
        join_req = get_object_or_404(TeamJoinRequest, id=request_id)
        team = join_req.team
        
        if request.user != team.owner:
            return redirect('team-list')
        
        join_req.status = 'rejected'
        join_req.save()
        
        return redirect('team-detail', pk=team.pk)