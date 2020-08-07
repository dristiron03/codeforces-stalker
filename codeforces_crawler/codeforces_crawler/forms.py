from django import forms
from django.forms import formset_factory

class UserIDForm(forms.Form):
    user = forms.CharField(required=True)

class PlagIDForm(forms.Form):
    contest = forms.IntegerField(required=True)
    submission = forms.IntegerField(required=True)

class CompareIDForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username here'
        }),
        required = True
    )

CompareIDFormset = formset_factory(CompareIDForm, extra=4)