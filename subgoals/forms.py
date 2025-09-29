from django import forms
from .models import Subtask

class SubgoalForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ["title", "description", "is_completed", "assigned_to"]