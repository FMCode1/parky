from django.urls import path
from . import views

urlpatterns = [
    path('signup_as/', views.signup_as, name='signup_as'),
    path('login_as/', views.login_as, name='login_as'),
    path('renter_signup/', views.renter_signup, name='renter_signup'),
    path('renter_login/', views.renter_login, name='renter_login'),
    path('host_signup/', views.host_signup, name='host_signup'),
    path('host_login/', views.host_login, name='host_login'),
    path('dashboard/renter/', views.renter_dashboard, name='renter_dashboard'),
    path('dashboard/host/', views.host_dashboard, name='host_dashboard'),
    path('logout/', views.logout, name='logout'),
]