from django import forms
from django.contrib.auth.models import User
from .models import PatientUser, StaffUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = PatientUser
        fields = ('gender',)


class StaffUserForm(forms.ModelForm):
    class Meta:
        model = StaffUser
        fields = ('job',)
