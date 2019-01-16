from django.contrib import admin
from .models import Topic
from .models import BlogPost

admin.site.register(Topic)
admin.site.register(BlogPost)