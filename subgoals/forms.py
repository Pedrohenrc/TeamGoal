from django import forms
from .models import SubGoal
from goals.models import Goal

class SubgoalForm(forms.ModelForm):
    class Meta:
        model = SubGoal
        fields = ["title", "description", "is_completed", "assigned_to"]
