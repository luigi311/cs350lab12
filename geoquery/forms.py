# forms.py

from django import forms
from django.forms import Form

class LookupForm(Form):
    location = forms.CharField(widget=forms.TextInput)