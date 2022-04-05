from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta



class WorkoutTimeofday(models.Model):
    workout_timeofday_name = models.CharField(max_length=30)

    def __str__(self):
        return self.workout_timeofday_name


class WorkoutPlan(models.Model):
    weekday_1 = models.DateTimeField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.weekday_1


class Workout(models.Model):
    workout_name = models.CharField(
        max_length=50,
        blank=True
    )
    workout_timeofday = models.ForeignKey(
        WorkoutTimeofday,
        on_delete=models.CASCADE
    )
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE
    )
    weekday = models.DateTimeField()
    

    def __str__(self):
        return self.workout_name