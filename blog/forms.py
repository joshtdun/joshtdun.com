from django import forms
from blog.models import Comment

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', ]


class ContactForm(forms.Form):
    email = forms.EmailField(label='Your email', help_text='A valid email please.')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    cc_myself = forms.BooleanField(label='Send Yourself a Copy', required=False)
