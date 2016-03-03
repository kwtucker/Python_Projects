from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("name")
        instance.save()
        messages.success(request, "Success")
        return HttpResponseRedirect(instance.get_absolute_url())
    context_data = {
        'form': form,
    }
    return render(request, "post_form.html", context_data)

def post_detail(request, id):
    instance = get_object_or_404(Post,id=id)
    context_data = {
        "name": instance.name,
        "instance": instance,
    }
    return render(request, "post_detail.html", context_data)

def post_list(request):
    queryset = Post.objects.all()
    context_data = {
            "object_list": queryset,
            "name": "List",
            "meetup_id": "List",
            "meetup_link": "List"
    }
    return render(request, "post_list.html", context_data)

def post_update(request, id):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context_data = {
        "name": instance.name,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context_data)

def post_delete(request, id):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")





