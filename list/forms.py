from django import forms
from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    relevant_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
