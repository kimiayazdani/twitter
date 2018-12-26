from django import forms
from twitterApp.models import TwitterUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'avatar']


