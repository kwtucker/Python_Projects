from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from .models import Post
import services

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # print form.cleaned_data.get("group_name")
        instance.save()
        messages.success(request, "Success Added")
        # return HttpResponseRedirect(instance.get_absolute_url())
        return redirect("posts:get")
    context_data = {
        'form': form,
    }
    return render(request, "post_form.html", context_data)

# def post_detail(request, id):
#     instance = get_object_or_404(Post,id=id)
#     context_data = {
#         "name": instance.group_name,
#         "instance": instance,
#     }
#     return render(request, "post_detail.html", context_data)

def post_list(request):
    queryset = Post.objects.all()
    context_data = {
            "object_list": queryset,
    }
    return render(request, "post_list.html", context_data)

def post_update(request, id):
    instance = get_object_or_404(Post,id=id)
    form = CommentForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        # return HttpResponseRedirect(instance.get_absolute_url())
        return redirect("posts:list")
    context_data = {
        "name": instance.group_name,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context_data)

def post_delete(request,id):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")


def get(request):
    events_list = services.get_events()
    context_data = {
        "instance": events_list,
    }
    return render(request,'events.html',context_data)


def post_comment(request, id):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    queryset = Post.objects.all()
    context_data = {
            "object_list": queryset,
            "instance": instance,
            "form":form,
    }

    return render(request, "post_list.html", context_data)



