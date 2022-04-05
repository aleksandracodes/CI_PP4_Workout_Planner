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
    weekday = models.DateTimeField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workout_plan'
    )

    def __str__(self):
        return self.pk


class Workout(models.Model):
    workout_name = models.CharField(
        max_length=50,
        blank=True
    )
    workout_time = models.ForeignKey(
        WorkoutTime,
        on_delete=models.CASCADE,
        related_name='workout_time'
    )
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name='workout_plan'
    )
    day = models.DateTimeField()

    def __str__(self):
        return self.workout_name
