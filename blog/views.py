from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import NewTopicForm
from blog.models import Topic
from blog.models import BlogPost

def home(request):
    return render(request, 'home.html')

def blog(request):
     blogposts = BlogPost.objects.all()
     topics =Topic.objects.all()
     return render(request, 'blog.html', {'blogposts': blogposts, 'topics':topics})

def topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})
  
def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'topic_detail.html', {'topic':topic})

def blog_detail(request):
    return render(request, 'blog_detail.html')

def about(request):
    return render(request, 'about.html')
