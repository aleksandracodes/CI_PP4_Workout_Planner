from django.shortcuts import render
from django.views.generic import ListView, View
from exercises.models import Exercise


class ExercisesView(ListView):
    model = Exercise
    template_name = "exercises/exercises-list.html"


class SingleExercise(View):
    def get(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        return render(request, 'exercises/exercise.html', 
                      {'exercise': exercise})
    
    
