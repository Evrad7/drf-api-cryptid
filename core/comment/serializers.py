


from ..user.serializers import UserSerializer
from ..post.models import Post
from ..user.models import User
from .models import Comment
from ..abstract.serializers import AbstractSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CommentSerializer(AbstractSerializer):
    author_id=serializers.SlugRelatedField(source="author",slug_field="public_id", queryset=User.objects.all(), many=False, write_only=True)
    author=UserSerializer(read_only=True)
    post=serializers.SlugRelatedField(slug_field="public_id", queryset=Post.objects.all(), many=False)


    def validate_author_id(self, value):
        # PB de sécurité ici résolu grâce au permissions
        if self.context["request"].user!=value:
            raise ValidationError("You can't manage a comment for another user")
        return value
    
    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value  
  
    def update(self, instance, validated_data):
        if not instance.edited:
            instance.edited=True
        return super().update(instance, validated_data)
    
    class Meta:
        model=Comment
        fields=["id", "body", "edited", "post", "author_id", "author", "created", "updated"]