from django.contrib.auth.models import Group

from .models import Tag, Task
from django.contrib import admin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content", )
    list_filter = ("is_done",)


admin.site.register(Tag)
admin.site.unregister(Group)
