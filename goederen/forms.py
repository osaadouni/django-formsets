from django import forms
from django.forms import inlineformset_factory

from .models import Goederen, GoederenNotitie

class GoederenForm(forms.ModelForm):
    class Meta:
        model = Goederen
        exclude = ()

class GoederenNotitieForm(forms.ModelForm):
    class Meta:
        model = GoederenNotitie
        exclude = ()

GoederenNotitieFormSet = inlineformset_factory(Goederen, GoederenNotitie,
                                            form=GoederenNotitieForm, extra=1
                                            )