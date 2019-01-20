from django.contrib import admin
from .models import Topic
from .models import BlogPost

admin.site.register(Topic)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'updated_at',
                     'created_at')