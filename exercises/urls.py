from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExercisesView.as_view()),
    path('show_exercise/<exercise_id>', views.SingleExercise.as_view(), name='show_exercise')
]
