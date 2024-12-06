

from ..user.models import User
from .models import Post
from .serializers import PostSerializer
from ..abstract.viewsets import AbstractViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend




class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method=="DELETE":
            return (obj.author==request.user)
        if request.method=="PUT":
            return obj.author==request.user
        return True

    def has_permission(self, request, view):

        if view.basename in ["post"]:
            if request.user.is_authenticated:
                return True
            if request.method in SAFE_METHODS:
                return True
        return False
    
class PostViewSet(AbstractViewSet):

    http_method_names=["get", "post", "put", "delete"]
    serializer_class=PostSerializer
    permission_classes=[UserPermission]
    lookup_field="public_id"
    filter_backends=[filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["author__public_id"]



    def get_queryset(self):
        return Post.objects.all()
    
    """ def get_object(self):
        super().get_object()
        public_id=self.kwargs["pk"]
        obj=User.objects.get_object_by_public_id(public_id)
        self.check_object_permissions(self.request, obj)
        return obj """
    
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        post=self.get_object()
        request.user.like(post)
        serializer=self.get_serializer_class()(post,  context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    @action(methods=['post'], detail=True)
    def dislike(self, request, *args, **kwargs):
        post=self.get_object()
        request.user.dislike(post)
        serializer=self.get_serializer_class()(post, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    