from .models import Contribution
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContributionForm
from goals.models import Goal
# Create your views here.

class ContributionCreateView(CreateView):
    model = Contribution
    form_class = ContributionForm
    """template_name"""

    def form_valid(self, form):
        form.instance.user = self.request.user
        goal_id = self.kwargs.get("pk")
        form.instance.goal = Goal.objects.get(pk=goal_id)
        return super().form_valid(form)

    def get_success_url(self):
        # depois de salvar, volta para a página da goal
        return reverse_lazy("goal-detail", kwargs={"pk": self.kwargs.get("pk")})

class ContributionListView(ListView, LoginRequiredMixin):
    Model = Contribution
    context_object_name = 'contributions'

    def get_queryset(self):
        queryset = Contribution.objects.all()

        status_param = self.request.GET.get("user")
        if status_param == "me":
            queryset = queryset.filter(user=self.request.user)
        
        goal_id = self.kwargs.get("pk")
        if goal_id:
            queryset = queryset.filter(pk=goal_id)
        
        return queryset

class ContributionDetailView(DetailView, LoginRequiredMixin):
    Model = Contribution
    """template_name"""
    context_object_name = "contribution"

class ContributionUpdateView(UpdateView, LoginRequiredMixin):
    Model = Contribution
    """template name"""

class ContributionDeleteView(DeleteView, LoginRequiredMixin):
    Model = Contribution
    """template_name = pagina de confirmar"""
    def get_success_url(self):
        return reverse_lazy("goal-detail", kwargs={"pk": self.kwargs.get("pk")})