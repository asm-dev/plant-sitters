from django.urls import path, include
from .views import (
    TaskListCreateView,
    TaskRetrieveUpdateView,
    TaskRetrieveDestroyView,
    TaskCustomView,
)
from .views_api import user_tasks, link_task_to_plantsitter

urlpatterns = [
    path('tasks/list_create/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/update/', TaskRetrieveUpdateView.as_view(), name='task-retrieve-update'),
    path('tasks/<int:pk>/delete/', TaskRetrieveDestroyView.as_view(), name='task-retrieve-destroy'),
    path('tasks/custom/', TaskCustomView.as_view(), name='task-custom'),
    path('user_tasks/<int:user_id>/', user_tasks, name='user_tasks'),
    path('link_task/<int:task_id>/plantsitter/<int:user_id>/', link_task_to_plantsitter, name='link_task_to_plantsitter'),
]
