from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    GenericAPIView,
)
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated
from tasks.models import Task
from tasks.serializers import TaskSerializer

class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return request.user.is_superuser or obj.requester == request.user
        return True
class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

class TaskRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrOwner]

class TaskCustomView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Task.objects.filter(is_completed=False)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)