from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Text']
        widgets = {
            'Text': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }

