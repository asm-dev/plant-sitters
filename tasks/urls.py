from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views_api import user_tasks

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_tasks/<int:user_id>/', user_tasks, name='user_tasks')
]
