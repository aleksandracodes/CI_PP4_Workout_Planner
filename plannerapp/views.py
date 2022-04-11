# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from django.forms import formset_factory
from datetime import timedelta

# Internal:
from .models import WorkoutPlan, WorkoutTime, Workout
from .forms import *
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
            return redirect('add_plan')
        
        else:
            workout_plan_form = WorkoutPlanForm()
            context = {'workout_plan_form': workout_plan_form}
        return render(request, 'plannerapp/planner.html', context)


class AddPlan(View):
    """
    A class view to display a page to add workout plan
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
        
        context = {'day1': day1,'day2': day2, 'day3': day3, 'day4': day4, 
                   'day5': day5,'day6': day6, 'day7': day7,'formset': formset,}
        return render(request, 'plannerapp/add_plan.html', context)


    def post(self, request):
        """
        A view to fill in the workout plan
        """           
        workout_plan_id = request.session.get('workout_plan.id')
        workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)
        
        day1 = workout_plan.first_day
        week = [
            day1,
            day1 + timedelta(days=1),
            day1 + timedelta(days=2),
            day1 + timedelta(days=3),
            day1 + timedelta(days=4),
            day1 + timedelta(days=5),
            day1 + timedelta(days=6),
        ]

        schedule_fields = formset_factory(WorkoutForm, extra=28)
        formset = schedule_fields(request.POST)

        if formset.is_valid():
            field = 0
            for form in formset:
                workout_name = form.cleaned_data.get('workout_name')
                if workout_name is None:
                    workout_name = ''
                workout_day = week[field % 7]
                
                if field < 14:
                    workout_time = WorkoutTime.objects.get(workout_time_name='AM')
                else:
                    workout_time = WorkoutTime.objects.get(workout_time_name='PM')
                
                workout = Workout(
                    workout_name=workout_name,
                    workout_time=workout_time,
                    workout_plan=workout_plan,
                    day=workout_day
                )
                workout.save()
                field += 1
            return redirect('planner_page')
        

class ViewPlans(generic.ListView):
    model = WorkoutPlan
    template_name = 'plannerapp/view_plans.html'
    paginate_by = 1
    
    def get_queryset(self):
        """
        Display workout plans for currently logged
        """
        return WorkoutPlan.objects.filter(user=self.request.user)


class EditPlan(View):
    def get(self, request):
        return render(request, 'plannerapp/edit_plan.html')
    
 