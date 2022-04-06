from django import forms
from .models import WorkoutTime, WorkoutPlan, Workout


class DateInput(forms.DateInput):
    input_type = 'date'


class WorkoutTimeForm(forms.ModelForm):

    class Meta:
        model = WorkoutTime
        fields = ('workout_time_name',)


class WorkoutPlanForm(forms.ModelForm):

    class Meta:
        model = WorkoutPlan
        fields = ('weekday',)
        widgets = {
            'weekday': DateInput(),
        }


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ('workout_name',)