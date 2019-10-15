from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import MyUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'url')