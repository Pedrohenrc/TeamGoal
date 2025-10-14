from .models import Contribution
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContributionForm
from goals.models import Goal
from subgoals.models import SubGoal
# Create your views here.

class ContributionCreateView(CreateView):
    model = Contribution
    form_class = ContributionForm
    template_name = "contributions/contribution_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        subtask_id = self.kwargs.get("subgoal_id")
        goal_id = self.kwargs.get("goal_id")

        if subtask_id:
            form.instance.subtask = SubGoal.objects.get(pk=subtask_id)
            form.instance.goal = form.instance.subtask.goal
        elif goal_id:
            form.instance.goal = Goal.objects.get(pk=goal_id)
        else:
            # erro: precisa de subtask ou goal
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        # depois de salvar, volta para a página da goal
        return reverse_lazy("goal-detail", kwargs={"pk": self.object.goal.pk})

class ContributionListView(ListView, LoginRequiredMixin):
    model = Contribution
    context_object_name = 'contributions'
    template_name = "contributions/contribution_list.html"  

    def get_queryset(self):
        queryset = Contribution.objects.all()

        status_param = self.request.GET.get("user")
        if status_param == "me":
            queryset = queryset.filter(user=self.request.user)
        
        goal_id = self.kwargs.get("goal_id")
        if goal_id:
            queryset = queryset.filter(goal_id=goal_id)
        
        return queryset

class ContributionDetailView(DetailView, LoginRequiredMixin):
    model = Contribution
    template_name = "contributions/contribution_detail.html"
    context_object_name = "contribution"

class ContributionUpdateView(UpdateView, LoginRequiredMixin):
    model = Contribution
    form_class = ContributionForm
    template_name = "contributions/contribution_form.html"

    def get_success_url(self):
        # redireciona para a goal associada
        return reverse_lazy("goal-detail", kwargs={"pk": self.object.goal.id})


class ContributionDeleteView(DeleteView, LoginRequiredMixin):
    model = Contribution
    template_name = "contributions/contribution_confirm_delete.html"
    def get_success_url(self):
        return reverse_lazy("goal-detail", kwargs={"pk": self.object.goal.pk})