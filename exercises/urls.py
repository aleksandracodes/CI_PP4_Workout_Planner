from django.urls import path
from exercises.views import ExercisesView

urlpatterns = [
    path('', ExercisesView.as_view()),
]
