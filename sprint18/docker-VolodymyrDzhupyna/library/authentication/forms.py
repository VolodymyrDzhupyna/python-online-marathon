from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegisterCustomUserModelForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required.'})
    middle_name = forms.CharField(required=False, label='Patronymic')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'role', 'email']
        labels = {'first_name': 'First name', 'last_name': 'Surname', 'role': 'Choose a role'}

    def save(self, commit=True):
        user = super(RegisterCustomUserModelForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        password = self.clean_password2()
        if commit:
            user.save()
        return user


class LoginCustomUserModelForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': 'Email is required.'})
    password = forms.CharField(widget=forms.PasswordInput())

