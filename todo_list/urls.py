from django.urls import path

from todo_list.views import TodoListView

app_name = 'todo_list'

urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
]