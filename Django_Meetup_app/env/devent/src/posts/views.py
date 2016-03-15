from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, CommentForm
from .models import Event
import services


### Create ###
    # When the request from the Add to List button on the templates/events.html is pressed
    # the API event will be add to the database and displayed to the templates/event_list.html
def event_create(request):
    # send the request object to the EventForm to grab the object data.
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully added to your list!")
        # Redirecting to /posts/get which is the same page the user is on.
        return redirect("posts:get")
    # setting the form request to an object and sending it to the event_form.html view.
    context_data = {
        'form': form,
    }
    return render(request, "event_form.html", context_data)

### Read ###
# Get all the objects from the database and send them to the event_list.html view
def event_list(request):
    queryset = Event.objects.all()
    context_data = {
            "object_list": queryset,
    }
    return render(request, "event_list.html", context_data)


### Update ###
    # The id of the object is passed through the url route.
    # When the Add Comment button is pressed the object will be set to instance.
    # Then it will display the form with only the comment textarea.
    # On Submit it will save it to that instance object and pass it to the view
def event_comment_update(request, id):
    instance = get_object_or_404(Event,id=id)
    form = CommentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return redirect("posts:list")
    context_data = {
        "name": instance.group_name,
        "instance": instance,
        "form":form,
    }
    return render(request, "event_form.html", context_data)


### Delete ###
    # The id of the object is passed through the url route.
    # The object is selected and deleted from the database.
    # Redirect back to the same page list.
def event_delete(request,id):
    instance = get_object_or_404(Event,id=id)
    instance.delete()
    messages.info(request, "Deleted")
    return redirect("posts:list")

### API GET ###
    # Get the api json and loop through the database and set the objects event_id to a list.
    # Pass both the json and array to the view.
    # If the api object id matches the id from the database the Add to list button will be changed to Attending.
def get(request):
    events_list = services.get_events()
    eventids = []

    # loops through database and appends all the event ids to a array
    # and sends it to the view to check if the id equals the api id then
    # changes the color and text, letting the user know they are attending.
    for e in Event.objects.all():
        eventids.append(e.event_id)

    context_data = {
        "instance": events_list,
        "eventids": eventids,
    }
    return render(request,'events.html',context_data)

# Grab the one object and set it to instance.
# sets the object to the corresponding form fields.
# grabs all the objects from the database.
# Pass everything to the event_list.html view
def event_comment(request, id):
    instance = get_object_or_404(Event,id=id)
    form = EventForm(request.POST or None, instance=instance)
    queryset = Event.objects.all()
    context_data = {
            "object_list": queryset,
            "instance": instance,
            "form":form,
    }
    return render(request, "event_list.html", context_data)



