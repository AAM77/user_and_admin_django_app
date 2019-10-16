from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView
)
from . import views

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/new/', UserCreateView.as_view(), name='user-create'),

]