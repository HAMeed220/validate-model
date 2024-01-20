from django import forms
from app.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    botcather=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)

def clean_botcather(self):
    b=self.cleaned_data['botcather']
    if len(b)>0:
        raise forms.ValidationError('boyt')
