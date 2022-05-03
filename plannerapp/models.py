# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import UniqueConstraint
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class WorkoutTime(models.Model):
    """
    A class for the WorkoutTime model
    """
    workout_time_name = models.CharField(max_length=50)

    def __str__(self):
        """
        Returns the workout time string
        """
        return self.workout_time_name


class WorkoutPlan(models.Model):
    """
    A class for the WorkoutPlan model
    """
    first_day = models.DateField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workout_plan'
    )

    class Meta:
        ordering = ['first_day']
        constraints = [
            UniqueConstraint(fields=['user', 'first_day'],
                             name='unique_start_date')
        ]

    def __str__(self):
        """
        Returns the first_day date
        """
        return datetime.strptime(format(self.first_day),
                                 '%Y-%M-%d').strftime('%d/%M/%Y')


class Workout(models.Model):
    """
    A class for the Workout model
    """
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
        """
        Returns the workout name string
        """
        return self.workout_name
