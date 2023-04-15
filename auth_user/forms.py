from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"}))

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'researcher', 'secretariat', 'stakeholder', 'is_superuser', 'first_name', 'last_name')

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control", "placeholder":"Username"}))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", "placeholder":"Password"}))
