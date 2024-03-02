from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            "content": forms.Textarea(attrs={
                'class': "form-control",
                "placeholder": "Message...",
                "cols": 45,
                "rows": 8
            })
        }
