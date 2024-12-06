from ..abstract.serializers import AbstractSerializer
from core.user.models import User
from django.conf import settings
from rest_framework import serializers


class UserSerializer(AbstractSerializer):
    posts_count=serializers.SerializerMethodField()



    def get_posts_count(self, instance):
        return instance.post_set.count()
    
       
    def to_representation(self, instance):
        user=super().to_representation(instance)
        if not user["avatar"]:
            request = self.context.get('request')
            user["avatar"]=request.build_absolute_uri(settings.DEFAULT_AVATAR_URL)
        return user
    
    def update(self, instance, validated_data):
        request=self.context.get("request")
        data=validated_data
        if request.method=="PATCH":
            data={}
            for _ in self.Meta.update_fields:
                field=validated_data.get(_)
                if field:
                    data[_]=field
        return super().update(instance, data)

    
    class Meta:
        model=User
        fields=["id", "username", "first_name", "last_name", "email","avatar", "posts_count",
                "is_active", "created", "updated"]
        update_fields=["avatar", "first_name", "last_name"]
        read_only_fields=["is_active", "created", "updated", "id"]
 
