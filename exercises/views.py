# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator

# Internal
from .models import Exercise
from .filters import ExerciseFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def show_all_exercises_page(request):
    """
    A view to show all exercises with pagination
    and continue pagination with filtered exercises
    """
    context = {}

    filtered_exercises = ExerciseFilter(
        request.GET,
        queryset=Exercise.objects.all()
    )

    context['filtered_exercises'] = filtered_exercises

    paginated_filtered_exercises = Paginator(filtered_exercises.qs, 12)

    page_number = request.GET.get('page')
    exercise_page_obj = paginated_filtered_exercises.get_page(page_number)

    context['exercise_page_obj'] = exercise_page_obj
    context['all_exercises'] = Exercise.objects.all()

    return render(request, 'exercises/exercises_list.html', context)


class SingleExercise(View):
    """
    A class view to display a single exercise
    """
    def get(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        return render(request, 'exercises/exercise.html',
                      {'exercise': exercise})
