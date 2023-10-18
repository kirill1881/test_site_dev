from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_email', 'oblast', 'city', 'gender', 'age', 'organization']
