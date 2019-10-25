from django import forms
from .models import Profile,Project
from django.contrib.auth.models import User


class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile',]   
