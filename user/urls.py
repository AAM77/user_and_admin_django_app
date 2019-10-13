from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/show_page', views.user_view, name='user-show'),
    path('users/new', views.user_create, name='user-create'),
    path('users/logout', views.user_logout, name='user-logout')
]