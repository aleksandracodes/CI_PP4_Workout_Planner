from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def loginPage(request):
    page ='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method =='POST':
        username = request.POST.get('username')
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
            messages.error(request, 'User name or password not exist')
        
    context = {'page' :page}
    return render(request, 'home/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    return render(request, 'home/login-register.html')


def home(request):
    return render(request, 'home/index.html')
