# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os

# Internal
from plannerapp.models import WorkoutPlan
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

        context = {
            'user': user,
            'plans_number': plans_number,
            'first_plan': first_plan,
            'last_plan': last_plan}
        return render(request, 'home/profile.html', context)

    else:
        messages.error(request,
                       "You don't have access to other user's details")
        return redirect('home')


def deleteUser(request, pk):
    """
    A view for deleting existing user
    """
    user = User.objects.get(username=pk)

    if request.method == "POST":
        user.delete()
        messages.info(request,
                      "Sorry to see you go. Your user has been deleted.")
        return redirect('home')


def contact(request):
    """
    A view to display user contact form
    """
    if request.method == "POST":
        message = request.POST['message']

        if request.user.is_authenticated:
            message_name = request.user.username
            message_email = request.user.email

            if request.user.email:
                message_email = request.user.email
            else:
                message_email = request.POST['message-email']

        else:
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']

        send_mail(
            'Message from ' + message_name +
            ' (' + message_email + ')',  # email subject
            message,  # message
            message_email,  # from email
            [os.environ.get('EMAIL_HOST_USER')],  # to email
        )

        context = {
            'message_name': message_name,
        }
        return render(request, 'home/contact.html', context)

    else:
        return render(request, 'home/contact.html', {})
