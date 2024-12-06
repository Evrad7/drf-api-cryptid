
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

from .models import Comment

from .serializers import CommentSerializer
from ..abstract.viewsets import AbstractViewSet

class UserPermissionComment(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method=="DELETE":
            return (request.user in [obj.author, obj.post.author]) | request.user.is_superuser
        if request.method=="PUT":
            return obj.author==request.user
        return True

    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        if request.method in SAFE_METHODS:
            return True
        return False
    
class CommentViewSet(AbstractViewSet):

    http_method_names=["get", "post","put", "delete"]
    serializer_class=CommentSerializer
    permission_classes=[UserPermissionComment]
    lookup_field="public_id"
    
    def get_queryset(self):
        post_public_id=self.kwargs.get("post_public_id")
        if post_public_id is None:
            return Http404
        return Comment.objects.filter(post__public_id=post_public_id)


    