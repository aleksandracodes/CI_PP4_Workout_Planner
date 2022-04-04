# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views.generic import ListView, View

# Internal
from .models import Exercise
from .filters import ExerciseFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ExercisesView(ListView):
    model = Exercise
    template_name = "exercises/exercises-list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ExerciseFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SingleExercise(View):
    def get(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        return render(request, 'exercises/exercise.html', {'exercise': exercise})