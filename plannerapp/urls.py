# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.PlannerView.as_view(), name='planner-page'),
    path('choose_date/', views.ChooseDate.as_view(), name='choose-date'),
    path('add_plan/', views.AddPlan.as_view(), name='add-plan'),
]