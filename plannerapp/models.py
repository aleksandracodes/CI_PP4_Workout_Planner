# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User


class WorkoutTime(models.Model):
    workout_time_name = models.CharField(max_length=50)

    def __str__(self):
        return self.workout_time_name


class WorkoutPlan(models.Model):
    first_day = models.DateField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workout_plan'
    )

    class Meta:
        ordering = ['first_day']
        
    def __str__(self):
        return 'workoutplan for {}'.format(self.first_day)


class Workout(models.Model):
    workout_name = models.CharField(
        max_length=50,
        blank=True,
        null=False,
        default='',
    )
    workout_time = models.ForeignKey(
        WorkoutTime,
        on_delete=models.CASCADE,
        related_name='workout_time'
    )
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name='plan'
    )
    day = models.DateField()

    
    def __str__(self):
        return self.workout_name
