from django import forms
from django.contrib.auth.models import User
from twitterApp.models import Profile

from captcha.fields import CaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'email', 'username', 'password',)
        fields = ('username', 'password', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)


class LoginWithCaptcha(forms.Form):
    captcha = CaptchaField()
