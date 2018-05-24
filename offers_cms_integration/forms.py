from django import forms

from application.models import Estate


class EstateWizardForm(forms.ModelForm):
    class Meta:
        model = Estate
        exclude = []