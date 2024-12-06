
from typing import Any, Dict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ...user.serializers import UserSerializer

class LoginSerilizer(TokenObtainPairSerializer):
    
    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data= super().validate(attrs)
        data["user"]=UserSerializer(self.user, context=self.context).data
        return data
