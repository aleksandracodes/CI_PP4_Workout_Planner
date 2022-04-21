# Imports
from plannerapp.models import WorkoutPlan, Workout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import messages
from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  

from django.core.mail import send_mail
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def home(request):
    """
    A view to display home page
    """
    return render(request, 'home/index.html')


def userProfile(request, pk):
    """
    A view to display user profile
    """
    user = User.objects.get(username=pk)
    
    if request.user == user:
        plans_number = WorkoutPlan.objects.filter(user=user).count
        first_plan = WorkoutPlan.objects.filter(user=user).first()
        last_plan = WorkoutPlan.objects.filter(user=user).last()

        context = {'user': user, 'plans_number':plans_number, 'first_plan':first_plan, 'last_plan':last_plan}
        return render(request, 'home/profile.html', context)
    
    else:
        messages.error(request, "You don't have access to other user's details")
        return redirect('home')


def deleteUser(request, pk):
    """
    A view for deleting existing user
    """
    user = User.objects.get(username=pk)

    if request.method == "POST":
        user.delete()
        messages.info(request, "Sorry to see you go. Your user has been deleted.")
        return redirect('home')


def contact(request):
    
    if request.method == "POST":
        message = request.POST['message']
        message_email = request.POST['message-email']
        
        if request.user.is_authenticated:
            message_name = request.user.username
        else:
            message_name = request.POST['message-name']

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