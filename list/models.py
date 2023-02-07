from django.db import models


class Tag(models.Model):
    task = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now=True, blank=True)
    done = models.BooleanField()
    not_relevant_tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )
