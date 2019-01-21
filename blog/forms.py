from django import forms
from blog.models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=250)

    class Meta:
        model = Topic
        fields = ['name', 'slug']