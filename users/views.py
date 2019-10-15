from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm, MyUserAuthenticationForm


def home_view(request):
    return render(request, 'users/home.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)

        # if all fields meet criteria save form & authenticate the user
        # login user & redirect to the home page (for now)
        # otherwise, fill in the form with the values & reload the page
        # display any errors in the template
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            login(request, user)
            return redirect('')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


# if the user is already authenticate, redirect to the user's home page ('home' for now)
# otherwise, if there's a POST request, get the form data, and check if valid
    # if valid, grab the email and password from the request & authenticate the user
        # if the user is authenticated, log in the user and render the user log in page
# else, fill out the form with with the passed in info & raise errors in the template
def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = MyUserAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return render(request, 'users/user_home.html', context)

    else:
        form = MyUserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)