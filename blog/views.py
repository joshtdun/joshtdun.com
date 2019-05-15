from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import NewComment
from blog.models import Topic
from blog.models import BlogPost, Comment
from blog.forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')

def blog(request):
     blogposts = BlogPost.objects.order_by('-updated_at')[:10]
     topics =Topic.objects.all()
     return render(request, 'blog.html', {'blogposts':blogposts, 'topics':topics})

def topics(request):
    topics = Topic.objects.all()  
    return render(request, 'topics.html', {'topics':topics})
  
def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'topic_detail.html', {'topic':topic})
    
def posts(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'posts.html', {'blogposts':blogposts})

def blogPost_detail(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    comments = Comment.objects.filter(blogPost=blogpost)
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogPost = blogpost
            comment.created_by = request.user
            comment.save()
            return redirect('blogPost_detail', slug=slug)
    else:
        form = NewComment()
    return render(request, 'blogPost_detail.html', {'blogpost':blogpost, 'comments':comments})

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

@login_required
def blogPost_reply(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    comments = Comment.objects.filter(blogPost=blogpost)
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogPost = blogpost
            comment.created_by = request.user
            comment.save()
            return redirect('blogPost_detail', slug=slug)
    else:
        form = NewComment()
    return render(request, 'blogPost_reply.html', {'blogpost':blogpost, 'form':form, 'comments':comments})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['josh@joshtdun.com']
        if cc_myself:
            recipients.append(sender)
         
        send_mail(subject, message, sender, recipients)
        return redirect('thanks')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})
