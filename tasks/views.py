from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tasks.models import Task
from tasks.serializers import TaskSerializer

class IsTaskOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return obj.created_by == request.user
        return True

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)