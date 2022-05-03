# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from .models import WorkoutTime, WorkoutPlan, Workout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):
    """
    A class for date input
    """
    input_type = 'date'


class WorkoutTimeForm(forms.ModelForm):
    """
    A class for WorkoutTime form
    """
    class Meta:
        model = WorkoutTime
        fields = ('workout_time_name',)


class WorkoutPlanForm(forms.ModelForm):
    """
    A class for WorkoutPlan form
    """
    class Meta:
        model = WorkoutPlan
        fields = ('first_day',)
        widgets = {
            'first_day': DateInput(),
        }


class WorkoutForm(forms.ModelForm):
    """
    A class for Workout form
    """
    class Meta:
        model = Workout
        fields = ('workout_name',)
        labels = {
                    "workout_name": "workout name"
                }
