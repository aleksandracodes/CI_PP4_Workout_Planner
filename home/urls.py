# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path

# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<str:pk>/', views.userProfile, name="profile"),
    path('contact/', views.contact, name="contact"),
    path('delete_user/<str:pk>', views.deleteUser, name='delete_user'),
]
