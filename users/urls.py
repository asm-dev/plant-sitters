from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActiveUserListView, UserListCreateView, UserRetrieveDestroyView, UserRetrieveUpdateView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('users/list-create/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/update/', UserRetrieveUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserRetrieveDestroyView.as_view(), name='user-delete'),
    path('users/active/', ActiveUserListView.as_view(), name='active-users'),
]