from .models import Task, Tag
from django.views.generic import ListView



class TodoListView(ListView):
    model = Task
    template_name = 'todolist/index.html'
