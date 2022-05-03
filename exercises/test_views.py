# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestExercisesViews(TestCase):
    """
    A class for testing exercises views
    """
    def test_get_exercise_page(self):
        """
        This test checks if the exercise page is displayed
        """
        response = self.client.get('/exercises/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exercises/exercises_list.html')
