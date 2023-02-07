from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
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
    form_class = TaskForm
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


def do_undo_task(request, task_id, param):
    task_obj = get_object_or_404(Task, id=task_id)

    if task_obj and param == "undo":
        task_obj.done = False
        task_obj.save()

    elif task_obj and param == "do":
        task_obj.done = True
        task_obj.save()

    return redirect("list:task-list")
