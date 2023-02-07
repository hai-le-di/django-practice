from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(auto_now=True, blank=True)
    done = models.BooleanField()
    relevant_tags = models.ManyToManyField(
        Tag,
        related_name="tasks"
    )

    class Meta:
        ordering = ['-done', '-created_at']
