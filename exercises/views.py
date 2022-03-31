from django.shortcuts import render
from .models import Exercise


def exercises(request):
    exercise_list = Exercise.objects.all
    return render(request, 'exercises/exercises.html', {'exercise_list': exercise_list})
