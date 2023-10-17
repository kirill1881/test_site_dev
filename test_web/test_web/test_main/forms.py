from django import forms
from .models import CustomUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('organization', 'e_mail', 'age', 'gender', 'oblast', 'city')

        # organization = forms.CharField(empty_value='Организация не указана')
        # e_mail = forms.EmailField(max_length=150)
        # GENDER_CHOICE = ('Мужчина', 'Женщина')
        # gender = forms.ChoiceField(choices=GENDER_CHOICE)
        # age = forms.IntegerField()
        # oblast = forms.CharField(max_length=300)
        # city = forms.CharField(max_length=200)
