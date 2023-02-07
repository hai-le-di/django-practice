from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    TagListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]


app_name = "list"
