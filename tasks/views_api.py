from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def user_tasks(request, user_id):
    tasks = Task.objects.filter(user_id=user_id)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
