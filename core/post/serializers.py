from xml.dom import ValidationErr
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..user.serializers import UserSerializer

from .models import Post
from ..user.models import User
from ..abstract.serializers import AbstractSerializer


class PostSerializer(AbstractSerializer):
    author_id=serializers.SlugRelatedField(source="author" ,slug_field="public_id", many=False, queryset=User.objects.all(), write_only=True)
    author=UserSerializer(read_only=True)
    liked=serializers.SerializerMethodField()
    likes_count=serializers.SerializerMethodField()

    def get_liked(self, instance):
        request=self.context.get("request", None)
        if not request:
            return False
        if not request.user.is_authenticated:
            return False
        return request.user.has_liked(instance)
    
    def get_likes_count(self, instance):
        return instance.liked_by.count()
        
         

    def validate_author_id(self, value):
        if self.context["request"].user!=value:
            raise ValidationError("You can't create a post for another user")
        return value
    
    def update(self, instance, validated_data):
        if not instance.edited:
            instance.edited=True
        instance=super().update(instance, validated_data)
        return instance

    class Meta:
        model=Post
        fields=["id", "author_id", "body",  "edited", "created", "updated", "author", "liked", "likes_count"]
        read_only_fields=["edited"]