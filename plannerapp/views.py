# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, View
from django.contrib import messages
from django.forms import formset_factory
from datetime import timedelta
from django.db import IntegrityError

# Internal:
from .models import WorkoutPlan, WorkoutTime, Workout
from .forms import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PlannerView(ListView):
    """
    A class view to show the planner page
    """
    def get(self, request):
        """
        Renders the home page
        """
        return render(request, 'plannerapp/planner.html')


class ChooseDate(View):
    """
    A class view to display a workout date picker
    """
    def get(self, request):
        """
        Renders the first day date picker for the planner
        """
        return render(request, 'plannerapp/choose_date.html',
                      {'workout_plan_form': WorkoutPlanForm()})

    def post(self, request):
        """
        Creates a new plan with the input from the workout_plan_form
        """
        workout_plan_form = WorkoutPlanForm(request.POST)

        if workout_plan_form.is_valid():
            user = request.user
            first_day = workout_plan_form.cleaned_data.get('first_day')
            workout_plan = WorkoutPlan(user=user, first_day=first_day,)

            try:
                workout_plan.save()
                # get workout plan ID
                request.session['workout_plan.id'] = workout_plan.pk
                return redirect('add_plan')

            except IntegrityError as e:
                messages.error(request,
                               'You already have a plan starting on this day.')
                return render(request, 'plannerapp/choose_date.html',
                              {'workout_plan_form': WorkoutPlanForm()})

        else:
            workout_plan_form = WorkoutPlanForm()
            context = {'workout_plan_form': workout_plan_form}

        return render(request, 'plannerapp/view_plans.html', context)


class AddPlan(View):
    """
    A class view to display a page to add workout plan
    """
    def get(self, request):
        """
        Display a field for each day to add a single workout
        """
        try:
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

            # 28 -> 4 rows for 7 days
            formset = formset_factory(WorkoutForm, extra=28)

            context = {'day1': day1, 'day2': day2, 'day3': day3, 'day4': day4,
                       'day5': day5, 'day6': day6, 'day7': day7,
                       'formset': formset, }
            return render(request, 'plannerapp/add_plan.html', context)

        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')

    def post(self, request):
        """
        Creates a new plan in the database
        from the input in formset
        """
        try:
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
                        workout_time = WorkoutTime.objects.get(
                            workout_time_name='AM')
                    else:
                        workout_time = WorkoutTime.objects.get(
                            workout_time_name='PM')

                    workout = Workout(
                        workout_name=workout_name,
                        workout_time=workout_time,
                        workout_plan=workout_plan,
                        day=workout_day
                    )
                    workout.save()
                    field += 1
                messages.success(request, 'Your plan has been created.')
                return redirect('view_plans')

        except:
            messages.error(request,
                           'Something went wrong when adding your plan...')
            return redirect('home')


class ViewPlans(generic.ListView):
    """
    A class view to render all plans for each user
    One plan displayed per page
    """
    model = WorkoutPlan
    template_name = 'plannerapp/view_plans.html'
    paginate_by = 1

    def get_queryset(self):
        """
        Display all plans from logged user
        """
        return WorkoutPlan.objects.filter(user=self.request.user)


class EditPlan(View):
    """
    A class view for editing existing plans for each user
    """
    def get(self, request, **kwargs):
        """
        Display a formset with fields corresponding to a specific plan id
        """
        try:
            workout_plan_id = self.kwargs['workout_plan_id']
            workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)

            day1 = workout_plan.first_day
            day2 = day1 + timedelta(days=1)
            day3 = day1 + timedelta(days=2)
            day4 = day1 + timedelta(days=3)
            day5 = day1 + timedelta(days=4)
            day6 = day1 + timedelta(days=5)
            day7 = day1 + timedelta(days=6)

            if request.user == workout_plan.user:
                workouts = Workout.objects.filter(workout_plan=workout_plan_id)
                schedule_fields = formset_factory(WorkoutForm, extra=0)
                field_value = []
                for workout in workouts:
                    field_value.append({'workout_name': workout.workout_name})
                formset = schedule_fields(initial=field_value)

                context = {'day1': day1, 'day2': day2, 'day3': day3,
                           'day4': day4, 'day5': day5, 'day6': day6,
                           'day7': day7, 'workout_plan': workout_plan,
                           'formset': formset, }

                return render(request, 'plannerapp/edit_plan.html', context)

            else:
                messages.info(request, "You cannot edit other user's plans.")
                return redirect('planner_page')

        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')

    def post(self, request, **kwargs):
        """
        Update plan in the database
        based on formset data
        """
        try:
            workout_plan = WorkoutPlan.objects.get(
                pk=self.kwargs['workout_plan_id'])

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
            workouts = Workout.objects.filter(workout_plan=workout_plan)

            if formset.is_valid():
                field = 0
                for form in formset:
                    if workouts:
                        workout_name = form.cleaned_data.get('workout_name')
                        workout = workouts[field]
                        workout.workout_name = workout_name
                        workout.save()

                    else:
                        workout_name = form.cleaned_data.get('workout_name')
                        if workout_name is None:
                            workout_name = ''
                        workout_day = week[field % 7]

                        if field < 14:
                            workout_time = WorkoutTime.objects.get(
                                workout_time_name='AM')
                        else:
                            workout_time = WorkoutTime.objects.get(
                                workout_time_name='PM')

                        workout = Workout(
                            workout_name=workout_name,
                            workout_time=workout_time,
                            workout_plan=workout_plan,
                            day=workout_day
                        )
                        workout.save()
                    field += 1
                messages.success(request, "Your plan has been amended.")
                return redirect('view_plans')
        except:
            messages.error(request, 'An error occurred...')
            return redirect('home')


class DeletePlan(View):
    """
    A class view for deleting existing plan
    """
    def post(self, request, **kwargs):
        """
        Deletes a selected plan
        """
        try:
            record = WorkoutPlan.objects.get(pk=self.kwargs['workout_plan_id'])
            if request.method == "POST":
                record.delete()
                messages.success(request, "Your plan has been deleted.")
                return redirect('view_plans')
        except:
            messages.error(request,
                           'An error occurred when deleting your plan.')
            return redirect('home')
