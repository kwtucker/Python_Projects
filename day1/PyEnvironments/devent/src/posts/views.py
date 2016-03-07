from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, CommentForm
from .models import Event
import services

def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully added to your list!")
        return redirect("posts:get")
    context_data = {
        'form': form,
    }
    return render(request, "event_form.html", context_data)

def event_list(request):
    queryset = Event.objects.all()
    context_data = {
            "object_list": queryset,
    }
    return render(request, "event_list.html", context_data)

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

def event_delete(request,id):
    instance = get_object_or_404(Event,id=id)
    instance.delete()
    messages.info(request, "Deleted")
    return redirect("posts:list")


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



