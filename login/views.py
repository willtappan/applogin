

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Forms


@login_required
def home(request):
    return render(request, "login/home.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid username and password'})

    return render(request, 'login/login.html')

