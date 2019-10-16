from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm, MyUserAuthenticationForm


#######################
# RENDER LANDING PAGE #
#######################
def home_view(request):
    return render(request, 'users/home.html')


##################################
# RENDER USER HOME PAGE ON LOGIN #
##################################
def user_home_view(request):
    return render(request, 'users/user_home.html')


###################################
# RENDER LOGOUT CONFIRMATION PAGE #
###################################
def logout_confirmation_view(request):
    return render(request, 'users/logout.html')


#########################################################################
# REGISTRATION: Handle Validation of Registration form & Authentication #
#########################################################################
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)

            login(request, user)
            return redirect('user_home')
            # return render(request, 'users/user_home.html', context)
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)


###########################################################
# LOGIN: Handle Validation of Login form & Authentication #
###########################################################
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
                if user.is_admin:
                    return redirect('admin:index')
                else:
                    return redirect('user_home')

    else:
        form = MyUserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)


##################
# HANDLE LOGOUT #
#################
def logout_view(request):
    logout(request)
    return redirect('logout_confirmation')