from django import forms

from poeditor.models import *

class PoForm(forms.ModelForm):
    class Meta:
        model = PoFile
        exclude = ['csv']
