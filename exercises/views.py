from django.views.generic import ListView
from exercises.models import Exercise


class ExercisesView(ListView):
    model = Exercise
    template_name = "exercises/exercises.html"