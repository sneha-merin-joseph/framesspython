# views.py
from django.shortcuts import render, redirect
from django.contrib import messages  # Import Django's messaging framework
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from  home.views import *

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')  # Success message
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')  # Error message
    else:
        form = RegistrationForm()
    return render(request, 'User-Page/Accounts/signup_form.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')  # Success message
            return redirect('home:index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')  # Error message
    else:
        form = LoginForm()
    return render(request, 'User-Page/Accounts/login_form.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')  # Success message
    return redirect('login')
