from wsgiref import validate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

#signup
class UserRegistrationForm(UserCreationForm):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDERS)
    phone_number = forms.CharField(label='Phone Number')

    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email']

    