from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SubGoal
from goals.models import Goal
from .forms import SubtaskForm
# Create your views here.
class SubtaskCreateView(LoginRequiredMixin, CreateView):
    model = SubGoal
    form_class = SubtaskForm

    def form_valid(self, form):
        goal_id = self.kwargs.get("pk")
        form.instance.goal = Goal.objects.get(pk=goal_id)
        return super().form_valid(form)

    def get_success_url(self):
         return reverse_lazy('goal-detail', kwargs={"pk": self.kwargs.get("pk")})