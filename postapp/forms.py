from django import forms
from .models import Profile
from django.contrib.auth.models import User


class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']