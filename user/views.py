from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Landing Page</h1>')

def user_view(request):
    return HttpResponse('<h1>User Show Page</h1>')

def user_create(request):
    return HttpResponse('<h1>User Create Form (Registration)</h1>')

def user_logout(request):
    # this should really be a session-delete function in
    # a session view that renders a confirmation page
    return HttpResponse('<h1>User Logged Out Confirmation Page</h1>')
