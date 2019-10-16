from django import forms
from users.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



############################
# Custom Registration form #
############################
class RegistrationForm(UserCreationForm):
    email   = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")
    url     = forms.CharField(max_length=255)

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'url')


    #####################################
    # Custom validation of email format #
    #####################################
    # Note: This is unnecessary
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("This is not a valid email. Format must be xx@xx.com")

        if '.com' not in email:
            raise forms.ValidationError("This is not a valid email. Format must be xx@xx.com")

        return email

    ###################################
    # Custom validation of url format #
    ###################################
    def clean_url(self, *args, **kwargs):
        url = self.cleaned_data.get('url')
        protocols = ['http://', 'https://']
        domain_names = ['.com', '.net', '.org']

        if all(protocol not in url for protocol in protocols):
            raise forms.ValidationError("This is not a valid url. Must include http:// or https://")

        if all(domain_name not in url for domain_name in domain_names):
            raise forms.ValidationError("This is not a valid url. Domain name must be .com, .net, or .org")
        return url



#########################################
# Custom validations for authentication #
#########################################
class MyUserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid email or password. Please double check and try again.")