from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")

        widgets = {
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
            }),
            "tags": forms.CheckboxSelectMultiple(attrs={
                "class": "form-select",
            }),
            "deadline": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            )
        }