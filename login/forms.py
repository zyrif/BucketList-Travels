from django import forms
from .models import UserInfo
from django.contrib.auth.models import User
# To-Do: Hash password rather than storing in plain text


class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), label='')

    class Meta:
        model = User
        fields = ('email', 'password')


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), label='')
    verify_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Re-type Password'}), label='')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')

        if password != verify_password:
            raise forms.ValidationError("Passwords do not match")


class UserInfoForm(forms.ModelForm):
    contactno = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Phone Number'}))

    class Meta:
        model = UserInfo
        fields = ('contactno',)
