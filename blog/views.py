from django.shortcuts import render
from blog.models import Topic

def home(request):
    return render(request, 'home.html')

def blog(request):
    topics = Topic.objects.all()
    return render(request, 'blog.html', {'topics': topics})

#def blog_topics(request, pk):
#    topic = Topic.objects.get(pk=pk)
#    return render(request, 'topics.html', {'topic': topic})