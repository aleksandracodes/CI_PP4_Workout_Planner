# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.models import User

# Internal:
from .models import WorkoutPlan
from .forms import WorkoutPlanForm, WorkoutForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PlannerView(ListView):
    """
    A class view to show the planner page
    """
    def get(self, request):
            return render(request, 'plannerapp/planner.html')


class ChooseDate(ListView):
    """
    A class view to display a workout date picker
    """
    def get(self, request):
        return render(request, 'plannerapp/choose-date.html', 
                      {'workout_plan_form': WorkoutPlanForm()})


    def selectWorkoutDate(request):
        if request.method == 'POST':
            workout_plan_form = WorkoutPlanForm(data=request.POST)
            if workout_plan_form.is_valid():
                user = request.user
                weekday = workout_plan_form.cleaned_data.get('weekday')
                workout_plan = WorkoutPlan(user=user, weekday=weekday,)
                workout_plan.save()
                return redirect('plannerapp/add-plan.html')
        else:
            workout_plan_form = WorkoutPlanForm()
            context = {'workout_plan_form': workout_plan_form}
            return render(request, 'plannerapp/choose-date.html', context)


class AddPlan(View):
    """
    A class view to display a page to add wokrout plan
    """
    def get(self, request):
        return render(request, 'plannerapp/add-plan.html', {'workout_form': WorkoutForm()})