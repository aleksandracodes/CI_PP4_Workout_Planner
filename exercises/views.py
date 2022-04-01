from django.shortcuts import render
from django.views.generic import ListView, View
from exercises.models import Exercise


class ExercisesView(ListView):
    model = Exercise
    template_name = "exercises/exercises-list.html"


class SingleExercise(View):
    template_name = 'exercises/exercise.html'
    def get(self, request, exercise_id, **kwargs):
        single_exercise = Exercise.objects.get(pk=exercise_id)
        return render(request, 'exercises/exercise.html', {'single_exercise': single_exercise})