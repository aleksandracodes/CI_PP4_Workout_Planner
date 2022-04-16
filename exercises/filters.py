# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
import django_filters

# Interal:
from .models import Exercise
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ExerciseFilter(django_filters.FilterSet):
    """
    A class for exercises filtering
    """
    name = django_filters.CharFilter(lookup_expr='icontains', label="Name")

    class Meta:
        model = Exercise
        fields = ['body_part', 'level', 'type']