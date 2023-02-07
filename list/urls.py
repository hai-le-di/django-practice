from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]


app_name = "list"
