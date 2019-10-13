from django.shortcuts import render

def home(request):
    return render(request,'user/home.html')

def user_view(request):
    return render(request, 'user/show.html')

def user_create(request):
    return render(request, 'user/new.html')

def user_logout(request):
    # this should really be a session-delete function in
    # a session view that renders a confirmation page
    return render(request, 'user/logout.html')
