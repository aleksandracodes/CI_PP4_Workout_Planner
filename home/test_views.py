# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class TestViews(TestCase):
    """
    A class for testing home view
    """
    def test_get_home_page(self):
        """
        This test checks if the index (home) page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class TestProfileView(TestCase):
    """
    A class for testing user profile page
    """
    def setUp(self):
        """
        This setup creates a test user
        """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

    def test_user_profile_page(self):
        """
        This test checks user profile page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/profile/test_user/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/profile.html')

    def test_delete_user(self):
        """
        Delete test user
        """
        User.objects.all().delete()


class TestContactForm(TestCase):
    """
    A class for testing contact form
    """
    def test_get_contact_page(self):
        """
        This tests display of the contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
        
    def test_sending_contact_form(self):
        """
        This test checks funcionality of the contact form
        """
        message = "test_user"
        subject = 'TestMessage'
        from_email = 'fromuser@mydjangoapp.com'
        recipient_list = ['toemail@youremail.com']
        
        mail.send_mail(
            message = message,
            subject = subject,
            from_email = from_email,
            recipient_list = recipient_list,
        )

        self.assertEqual(len(mail.outbox), 1)
