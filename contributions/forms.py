from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['progress']

        def clean_progress_value(self):
            value = self.cleaned_data['progress_value']
            if value < 0:
                raise forms.ValidationError("O progresso não pode ser negativo")
            return value