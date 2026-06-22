from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from list.forms import TaskForm
from list.models import Task, Tag
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View


class TodoListView(ListView):
    model = Task
    template_name = "todolist_templates/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by("is_done", "-date")


class TagsListView(ListView):
    model = Tag
    template_name = 'todolist_templates/tags.html'
    context_object_name = 'tags'


class AddTagsView(CreateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('todolist_templates:tags')
    template_name = "todolist_templates/add_tags.html"


class UpdateTagsView(UpdateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('todolist_templates:tags')
    template_name = "todolist_templates/add_tags.html"


class DeleteTagsView(DeleteView):
    model = Tag
    success_url = reverse_lazy('todolist_templates:tags')
    template_name = "todolist_templates/delete_tags.html"

class AddTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist_templates/add_task.html"
    success_url = reverse_lazy("todolist_templates:index")


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist_templates/add_task.html"
    success_url = reverse_lazy("todolist_templates:index")


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "todolist_templates/delete_task.html"
    success_url = reverse_lazy("todolist_templates:index")



class ToggleDoneView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)

        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])

        return redirect("todolist_templates:index")
