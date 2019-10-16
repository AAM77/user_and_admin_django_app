from django.urls import path
from .views import UserListView
from . import views

urlpatterns = [
    path('users', UserListView.as_view(), name='users-list'),
]