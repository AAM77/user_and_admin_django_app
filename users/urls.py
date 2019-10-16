from django.urls import path
from .views import UserListView, UserDetailView
from . import views

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]