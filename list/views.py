from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Tag, Task


def index(request):
    """View function for the home page of the site."""
    task_list = Task.objects.all()

    context = {
        "task_list": task_list,
    }

    return render(request, "list/task_list.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:tag-list")
