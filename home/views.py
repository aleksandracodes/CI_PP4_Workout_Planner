# Imports
from plannerapp.models import WorkoutPlan, Workout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def userProfile(request, pk):
    """
    A view to display user profile
    """
    user = User.objects.get(username=pk)
    
    if request.user == user:
    # ALL plans for all users
        plans_number = WorkoutPlan.objects.all().count
        first_plan = WorkoutPlan.objects.first()
        last_plan = WorkoutPlan.objects.last()

        context = {'user': user, 'plans_number':plans_number, 'first_plan':first_plan, 'last_plan':last_plan}
        return render(request, 'home/profile.html', context)
    
    else:
        messages.error(request, "You don't have access to other user's details")
        return redirect('home')


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
            messages.success(request, "You've been successfully logged in.")
            return redirect('planner_page')
        else:
            messages.error(request, "User name or password don't exist")
        
    context = {'page': page}
    return render(request, 'home/login-register.html', context)


def logoutUser(request):
    """
    A view to log out the user
    """
    logout(request)
    messages.info(request, "You have logged out.")
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
            messages.success(request, "Registration has been successful.")
            return redirect('planner_page')
        else:
            messages.error(request, 'An error occurred during registration.')   
    
    return render(request, 'home/login-register.html', {'form': form})


def home(request):
    """
    A view to display home page
    """
    return render(request, 'home/index.html')


def contact(request):
    if request.method == "POST":
        message = request.POST['message']
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']

        
        send_mail(
            'Message from ' + message_name + ' (' + message_email + ')', # email subject
            message, # message
            message_email, # from email
            ['aleksandracoding@gmail.com'], # to email
        )
        
        context = {
            'message_name':message_name,
        }
        return render(request, 'home/contact.html', context)
    
    else:
        return render(request, 'home/contact.html', {})