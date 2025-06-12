from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RenterSignupForm, HostSignupForm  # ✅ Import the forms

# Landing pages
def signup_as(request):
    return render(request, 'accounts/signup_as.html')

def login_as(request):
    return render(request, 'accounts/login_as.html')

def renter_signup(request):
    form = RenterSignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts:renter_login')  # 👈 Redirect to login after signup
    return render(request, 'accounts/renter_signup.html', {'form': form})


def host_signup(request):
    form = HostSignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts:host_login')  # 👈 Redirect to login after signup
    return render(request, 'accounts/host_signup.html', {'form': form})

# Renter login
def renter_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        # Optional role check: if hasattr(user, 'is_renter') and user.is_renter:
        login(request, user)
        return redirect('accounts:renter_dashboard')  # Change to your actual view name
    return render(request, 'accounts/renter_login.html', {'form': form})

# Host login
def host_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        # Optional role check: if hasattr(user, 'is_host') and user.is_host:
        login(request, user)
        return redirect('accounts:host_dashboard')
    return render(request, 'accounts/host_login.html', {'form': form})

@login_required
@login_required
def renter_dashboard(request):
    if not request.user.is_renter:
        return redirect('accounts:login_as')

    section = request.GET.get('section', 'default')
    return render(request, 'accounts/renter_dashboard.html', {'section': section})


@login_required
def host_dashboard(request):
    return render(request, 'accounts/host_dashboard.html')

def logout(request):
    logout(request)
    return redirect('accounts:login_as')  # Redirect after logout