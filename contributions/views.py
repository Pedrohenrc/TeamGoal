from .models import Contribution
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContributionForm
# Create your views here.

class ContributionCreateView (CreateView, LoginRequiredMixin):
    model = Contribution
    form_class = ContributionForm
    sucess_url = reverse_lazy("")