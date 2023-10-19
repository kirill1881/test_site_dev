from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_email', 'oblast', 'city', 'gender', 'age', 'organization']


# class QuestionForm(forms.Form):
#     # class Meta:
#     #     model = Question
#     #     fields = ['__all__']
#
#     user_answer = forms.ChoiceField(choices=Question.ANSWERS_CHOICE, widget=forms.RadioSelect)
#