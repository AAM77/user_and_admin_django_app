from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import RegistrationForm


def home_view(request):
    return render(request, 'users/home.html')

def registration_view(request):
    context = {}
    return render(request, 'users/register.html', context)