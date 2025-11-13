from django import forms
from .models import SubGoal
from goals.models import Goal
from django.contrib.auth import get_user_model

User = get_user_model()
class SubgoalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.goal = kwargs.pop('goal', None) 
        super().__init__(*args, **kwargs)

        if self.goal and self.goal.team:
            self.fields['assigned_to'].queryset = User.objects.filter(teams=self.goal.team).order_by('username')
        else:
            self.fields['assigned_to'].queryset = User.objects.none()
            
        self.fields['assigned_to'].empty_label = "Selecione um membro do time (Opcional)"
    class Meta:
        model = SubGoal
        fields = ["title", "description", "assigned_to"]
        

