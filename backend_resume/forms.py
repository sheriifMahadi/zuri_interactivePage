from django import forms
from django.db import models 
from .models import Comment

class MessageForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']

        widgets = {
            'comment': forms.Textarea
            (attrs={'placeholder': "Send me a message", 'class': 'message', 'cols': 70}),

            'name': forms.TextInput
            (attrs={'placeholder': "Your name", 'class': 'name'}),

             'email': forms.TextInput
            (attrs={'placeholder': "Your email", 'class': 'email'})}
    
        labels = {'name': '', 'email': '', 'comment': ''}