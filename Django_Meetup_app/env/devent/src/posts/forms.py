from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        # The model is for the Meta class to reference the stucture of the form with
        # expected Data types
        model = Event
        fields = [
            "group_name",
            "event_name",
            "event_date",
            "event_id",
            "event_url",
        ]

# When this class is call the form will only contain the comment field.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            "comment",
        ]