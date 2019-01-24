from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.slug

class BlogPost(models.Model):
    title = models.CharField(max_length=500, unique=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000, unique=True)
    message = models.TextField()
    topics = models.ManyToManyField(Topic)
    author = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='blogPosts', on_delete='cascade')
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete='cascade')
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return self.slug
        
class Comment(models.Model):
    message = models.TextField(max_length=4000)
    blogPost = models.ForeignKey(BlogPost, related_name='comment', on_delete='cascade')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comment', on_delete='cascade')
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete='cascade')    

    def __str__(self):
        return self.message