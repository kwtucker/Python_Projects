from django.contrib import admin

# Importing the Event class from the models directory in current directory
from .models import Event

class PostModelAdmin(admin.ModelAdmin):
    # This is what I will show in the admin view.
    list_display = ['group_name','event_name','event_date','event_id','event_url', 'comment']

    # This will reference the model Event class for data type
    class Meta:
        model = Event
admin.site.register(Event, PostModelAdmin)

