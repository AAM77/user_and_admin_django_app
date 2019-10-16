from django import forms
from users.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email   = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")
    url     = forms.CharField(max_length=255)

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'url')


    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not '@' in email and not '.com' in email:
            raise forms.ValidationError("This is not a valid email")
        return email

    def clean_url(self, *args, **kwargs):
        url = self.cleaned_data.get('url')
        protocols = ['http://', 'https://']
        domain_names = ['.com', '.net', '.org']

        if all(protocol not in url for protocol in protocols):
            raise forms.ValidationError("This is not a valid url. Must include http:// or https://")

        if all(domain_name not in url for domain_name in domain_names):
            raise forms.ValidationError("This is not a valid url. Domain name must be .com, .net, or .org")
        return url

# Create a custom form for authentication/login
# Meta specifies user model & fields of the form
# clean displays validation error if the fields are invalid
class MyUserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")