from django.shortcuts import render, get_object_or_404
from blog.models import Topic
from blog.models import BlogPost

def home(request):
    return render(request, 'home.html')

def blog(request):
     blogposts = BlogPost.objects.all()
     topics =Topic.objects.all()
     return render(request, 'blog.html', {'blogposts': blogposts, 'topics':topics})

def blog_topics(request):
    topics = Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})
    
def about(request):
    return render(request, 'about.html')