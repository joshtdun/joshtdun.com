from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=500, unique=False)
    message = models.TextField(max_length=10000)
    topics = models.ManyToManyField(Topic)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='blogPosts', on_delete='cascade')
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete='cascade')
    
    def __str__(self):
        return self.title
        

class Comment(models.Model):
    message = models.TextField(max_length=4000)
    blogPost = models.ForeignKey(Topic, related_name='comment', on_delete='cascade')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='comment', on_delete='cascade')
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete='cascade')    
