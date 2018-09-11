from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import models
from datetime import datetime, timezone

from groups.models import Group, Chat_Entry

from .helpers import get_dt

class NewAnnouncementForm(forms.Form):
    #see the description for title in models.py
    title = forms.CharField(label='Title', max_length=120, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
    #see the description for description in models.py
    description = forms.CharField(label='Description', max_length=120, widget=forms.TextInput(
        attrs={'type': 'text',
               'class': 'form-control'}))
