'''
Tests from https://github.com/sibtc/django-beginners-guide/tree/master/accounts/tests
Check out https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/
A Great Extremely Thorough Tutorial!
'''
from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='josh', email='josh@doe.com', password='123')
        self.response = self.client.post(reverse('password_reset'), { 'email': 'josh@doe.com' })
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[joshtdun.com] Password Reset Email', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('josh', self.email.body)
        self.assertIn('josh@doe.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['josh@doe.com',], self.email.to)