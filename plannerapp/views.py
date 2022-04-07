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


class ChooseDate(View):
    """
    A class view to display a workout date picker
    """
    def get(self, request):
        return render(request, 'plannerapp/choose_date.html', 
                      {'workout_plan_form': WorkoutPlanForm()})


    def post(self, request):
        """
         A view to select the workout start date
        """        
        workout_plan_form = WorkoutPlanForm(request.POST)
            
        if workout_plan_form.is_valid():
            user = request.user
            first_day = workout_plan_form.cleaned_data.get('first_day')
            workout_plan = WorkoutPlan(user=user, first_day=first_day,)
            workout_plan.save()
            return redirect('add_plan')
        
        else:
            workout_plan_form = WorkoutPlanForm()
            context = {'workout_plan_form': workout_plan_form}
        return render(request, 'plannerapp/planner.html', context)
        


class AddPlan(View):
    """
    A class view to display a page to add wokrout plan
    """
    def get(self, request):
        return render(request, 'plannerapp/add_plan.html', {'workout_form': WorkoutForm()})