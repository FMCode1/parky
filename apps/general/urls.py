from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('find_parking/', views.find_parking, name='find_parking'),
    path('list_parking/', views.list_parking, name='list_parking'),
    path('support/', views.support, name='support'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]