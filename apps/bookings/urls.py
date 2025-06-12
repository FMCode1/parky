from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='list'),
    path('new/', views.booking_create, name='create'),
    path('<int:pk>/edit/', views.booking_update, name='update'),
    path('<int:pk>/delete/', views.booking_delete, name='delete'),
]