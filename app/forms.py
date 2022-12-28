from django import forms
from django.core import validators
def check_for_q(value):
    if value[0].upper()=='Q':
        raise forms.ValidationError('not starts with q')
class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_q])
    father_name=forms.CharField(max_length=100,validators=[check_for_q])
    email=forms.EmailField()
    reemail=forms.EmailField()
    