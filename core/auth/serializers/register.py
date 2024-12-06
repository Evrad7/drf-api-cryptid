

from rest_framework import serializers
from ...user.models import User
from ...user.serializers import UserSerializer


class RegisterSerializer(UserSerializer):
    password=serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    class Meta:
        model=User
        fields=[ "id", "username", "first_name", "last_name", "email", "password", "avatar"]
        read_only_fields=["avatar"]
    
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    