from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import User
from .serializers import UserSerializer

class UserBaseView:
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserListCreateView(UserBaseView, ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_plantsitter', 'is_requester']
    search_fields = ['username', 'email']

class UserRetrieveUpdateView(UserBaseView, RetrieveUpdateAPIView):
    pass

class UserRetrieveDestroyView(UserBaseView, RetrieveDestroyAPIView):
    pass

class ActiveUserListView(UserBaseView, ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)

class UserViewSet(UserBaseView, ModelViewSet):
    pass
