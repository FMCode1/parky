# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'general/home.html')

def find_parking(request):
    return render(request, 'general/find_parking.html')

def list_parking(request):
    return render(request, 'general/list_parking.html')

def support(request):
    return render(request, 'general/support.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'accounts/login.html')