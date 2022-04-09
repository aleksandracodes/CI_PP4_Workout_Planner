# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.PlannerView.as_view(), name='planner_page'),
    path('choose_date/', views.ChooseDate.as_view(), name='choose_date'),
    path('add_plan/', views.AddPlan.as_view(), name='add_plan'),
    path('view_plans/', views.ViewPlans.as_view(), name='view_plans'),
]