from django.shortcuts import render
from django.views import generic

from .models import Tag, Task


def index(request):
    """View function for the home page of the site."""

    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "list/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
