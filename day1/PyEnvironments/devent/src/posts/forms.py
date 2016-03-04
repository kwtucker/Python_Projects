from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "group_name",
            "event_name",
            "event_date",
            "event_id",
            "event_url",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            "comment",
        ]