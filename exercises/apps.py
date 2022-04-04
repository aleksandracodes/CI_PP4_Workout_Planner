# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ExerciseConfig(AppConfig):
    """
    A class for configuring the exercises app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exercises'
