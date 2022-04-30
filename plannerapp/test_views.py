# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import WorkoutPlan
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestPlannerViews(TestCase):
    """
    A class for testing planner view
    """
    def test_get_planner_page(self):
        """
        This test checks if the planner page is displayed
        """
        response = self.client.get('/planner/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plannerapp/planner.html')
