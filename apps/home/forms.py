from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        readonly_fields = ('owner',)
        fields = ['comm', 'star']


class ContactForm(forms.Form):
    name = forms.CharField(max_length = 255)
    subject = forms.CharField(max_length = 255)
    message = forms.CharField(max_length = 1000)