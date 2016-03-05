from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "group_name",
            "event_name",
            "event_date",
            "event_id",
            "event_url",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            "comment",
        ]