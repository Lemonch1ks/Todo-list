from django.urls import path

from list.views import (
    TodoListView,
    TagsListView,
    AddTask,
    AddTagsView,
    UpdateTagsView,
    DeleteTagsView,
    UpdateTaskView,
    DeleteTaskView,
    toggle_done,

)

app_name = 'list'

urlpatterns = [
    path('', TodoListView.as_view(), name='index'),
    path('toggle_status/<int:pk>/', toggle_done, name='toggle_status'),

    path('tags/', TagsListView.as_view(), name='tags'),
    path('tags/add', AddTagsView.as_view(), name='add_tags'),
    path('tags/<int:pk>/update/', UpdateTagsView.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', DeleteTagsView.as_view(), name='tags_delete'),

    path('task_add/', AddTask.as_view(), name='add_task'),
    path('task_update/<int:pk>/', UpdateTaskView.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', DeleteTaskView.as_view(), name='task_delete'),

]
