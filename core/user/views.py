from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..abstract.viewsets import AbstractViewSet

from .models import User

from .serializers import UserSerializer
# Create your views here.


class UserViewSet(AbstractViewSet):
    http_method_names=["patch", "get"]
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        user=User.objects.get_object_by_public_id(self.kwargs.get("pk"))
        self.check_object_permissions(self.request, user)
        return user
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)

    
