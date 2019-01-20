from django.shortcuts import render, get_object_or_404
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
    topic = Topic.objects.get(slug=slug)
    return render(request, 'topic_detail.html', {'topic':topic})

def blog_detail(request):
    return render(request, 'blog_detail.html')

def about(request):
    return render(request, 'about.html')