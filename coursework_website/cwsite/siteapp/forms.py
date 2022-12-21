from django.forms import ModelForm
from django import forms
from .models import *

class ProteinForm(forms.Form):
    protein_id = forms.CharField(label="Protein Id", max_length=10)
    length = forms.IntegerField()

    class Meta:
        model = Protein
        fields = ['protein_id', 'protein_sequence', 'length' , 'organism_id']