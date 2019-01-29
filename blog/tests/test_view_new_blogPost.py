'''
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import BlogPost
import datetime

class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        user= User.objects.create(username='josht', password='123', email='josht@testemail.com')
        BlogPost.objects.create(title='Django Test', description='Django Test Post.', created_by=user, 
        updated_by=user , created_at='2019.01.19 15:00', updated_at='2019-01-19 15:00', 
        slug='django-test', message='there are alot of attributes', author='Josh')
        self.url = reverse('blogPost_detail', BlogPost.slug)
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
'''