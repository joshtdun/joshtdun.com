from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import home, blog, blog_topics
from .models import Topic


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
        
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home) 
        
        
class BlogTopicsTests(TestCase):
    def setUp(self):
        Topic.objects.create(name='Django')

    def test_blog_topics_view_not_found_status_code(self):
        url = reverse('blog_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_blog_topics_url_resolves_blog_topics_view(self):
        view = resolve('/blog/1/')
        self.assertEquals(view.func, blog_topics)