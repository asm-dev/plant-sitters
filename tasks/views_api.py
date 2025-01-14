from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from users.models import User
from rest_framework import status

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_tasks(request, user_id):
    tasks = Task.objects.filter(requester_id=user_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def link_task_to_plantsitter(request, task_id, user_id):
    try:
        task = Task.objects.get(id=task_id)
        user = User.objects.get(id=user_id)
        if not user.is_plantsitter:
            return Response({"error": "User is registered as a plantsitter"}, status=status.HTTP_400_BAD_REQUEST)
        task.plantsitter = user
        task.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
