from dataclasses import fields
from operator import contains
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User, AssessmentTest


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email',
                  'password', 'password1', 'address', 'phone', 'city', 'province', 'zipcode', 'country']
        widgets = {
            'password': forms.PasswordInput(),
            'password1': forms.PasswordInput(),
        }

    def clean_email(self):
        print(type(self.cleaned_data))
        email = self.cleaned_data.get('email')
        val = "@"
        if not val in email:
            raise forms.ValidationError("Email address is not valid")
        return email


class RegisterSpecialist(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email',
                  'password', 'password1', 'address', 'phone', 'category', 'specialist_id', 'city', 'province', 'zipcode', 'country']

        widgets = {
            'password': forms.PasswordInput(),
            'password1': forms.PasswordInput(),
        }


class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }


class SaveQuestions(forms.ModelForm):
    class Meta:
        model = AssessmentTest
        fields = ['username', 'answer_1', 'answer_2', 'answer_3', 'answer_4',
                  'answer_5', 'answer_6', 'answer_7', 'answer_8', 'answer_9']

        widgets = {
            'answer_1': forms.RadioSelect(),
            'answer_2': forms.RadioSelect(),
            'answer_3': forms.RadioSelect(),
            'answer_4': forms.RadioSelect(),
            'answer_5': forms.RadioSelect(),
            'answer_6': forms.RadioSelect(),
            'answer_7': forms.RadioSelect(),
            'answer_8': forms.RadioSelect(),
            'answer_9': forms.RadioSelect(),
        }
