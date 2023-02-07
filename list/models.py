from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now=True, blank=True)
    done = models.BooleanField()
    not_relevant_tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )


class Tag(models.Model):
    tasks = models.ManyToManyField(Task, related_name="tags")
