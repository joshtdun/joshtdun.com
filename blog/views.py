from django.shortcuts import render, get_object_or_404
from blog.models import Topic

def home(request):
    return render(request, 'home.html')

def blog(request):
    topics = Topic.objects.all()
    return render(request, 'blog.html', {'topics': topics})

def blog_topics(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'topics.html', {'topic': topic})
    
def about(request):
    return render(request, 'about.html')