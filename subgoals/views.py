from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubGoal
from goals.models import Goal
from .forms import SubgoalForm
# Create your views here.
class SubgoalCreateView(LoginRequiredMixin, CreateView):
    model = SubGoal
    form_class = SubgoalForm
    template_name = "subgoals/subgoal_form.html"

    def form_valid(self, form):
        goal_id = self.kwargs.get("pk")
        form.instance.goal = Goal.objects.get(pk=goal_id)
        return super().form_valid(form)

    def get_success_url(self):
         return reverse_lazy('goal-detail', kwargs={"pk": self.kwargs.get("pk")})
    
class SubgoalDetailView(LoginRequiredMixin, DetailView):
    model = SubGoal
    context_object_name = "subgoal"
    template_name = "subgoals/subgoal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contributions'] = self.object.contributions.all()

        return context
    
class SubgoalUpdateView(LoginRequiredMixin, UpdateView):
    model = SubGoal
    fields = ['title', 'description', 'assigned_to', 'is_completed']
    template_name = "subgoals/subgoal_list.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.goal.update_progress()
        return response
    
class SubgoalListView(LoginRequiredMixin, ListView):
    model = SubGoal
    context_object_name = "subgoals"
    template_name = "subgoals/subgoal_confirm_delete.html"

    def get_queryset(self):
        goal_id = self.kwargs["goal_id"]
        queryset = SubGoal.objects.filter(goal_id=goal_id)
        user = self.request.GET.get('user')
        if user:
            queryset = queryset.filter(assigned_to__id=user)
        return queryset

class SubgoalDeleteView(DeleteView):
    model = SubGoal

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        goal = self.object.goal           # pega meta antes de deletar
        response = super().delete(request, *args, **kwargs)
        goal.update_progress()            # atualiza progresso depois da exclusão
        return response

    def get_success_url(self):
        return reverse_lazy('goal-detail', kwargs={'pk': self.object.goal.id})
    

