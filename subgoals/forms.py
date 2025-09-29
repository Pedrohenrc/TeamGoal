from django import forms
from .models import SubGoal

class SubgoalForm(forms.ModelForm):
    class Meta:
        model = SubGoal
        fields = ["title", "description", "is_completed", "assigned_to"]