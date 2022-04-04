# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def userProfile(request, pk):
    """
    A view to display user profile
    """
    user = User.objects.get(username=pk)
    return render(request, 'home/profile.html', {'user': user})


def loginPage(request):
    """
    A view to display user profile
    """
    page ='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method =='POST':
        username = request.POST.get('username').capitalize()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User name or password don't exist")
        
    context = {'page': page}
    return render(request, 'home/login-register.html', context)


def logoutUser(request):
    """
    A view to log out the user
    """
    logout(request)
    return redirect('home')


def registerPage(request):
    """
    A view to register new user
    """
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.capitalize()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')   
    
    return render(request, 'home/login-register.html', {'form': form})


def home(request):
    """
    A view to display home page
    """
    return render(request, 'home/index.html')
