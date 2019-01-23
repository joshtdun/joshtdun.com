'''
Tests from https://github.com/sibtc/django-beginners-guide/tree/master/accounts/tests
Check out https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/
A Great Extremely Thorough Tutorial!
'''
from django.test import TestCase
from accounts.forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)