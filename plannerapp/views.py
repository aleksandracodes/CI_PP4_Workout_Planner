# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from django.forms import formset_factory
from datetime import timedelta

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
            
            # get workout plan ID
            request.session['workout_plan.id'] = workout_plan.pk
            print(workout_plan.pk)
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
        # based on the current session ID (first day of schedule)
        workout_plan_id = request.session.get('workout_plan.id')
        workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)
        day1 = workout_plan.first_day    
        day2 = day1 + timedelta(days=1)
        day3 = day1 + timedelta(days=2)
        day4 = day1 + timedelta(days=3)
        day5 = day1 + timedelta(days=4)
        day6 = day1 + timedelta(days=5)
        day7 = day1 + timedelta(days=6)
        
        formset = formset_factory(WorkoutForm, extra=28) # 28 -> 4 rows for 7 days
        
        print(workout_plan_id)
        print(workout_plan)
        print(day7)
        context = {'day1': day1,'day2': day2, 'day3': day3, 'day4': day4, 
                   'day5': day5,'day6': day6, 'day7': day7,'formset': formset,}
        return render(request, 'plannerapp/add_plan.html', context)
