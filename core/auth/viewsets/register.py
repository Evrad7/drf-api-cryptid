
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.register import RegisterSerializer

class RegisterViewSet(ViewSet):
    
    serializer_class=RegisterSerializer
    http_method_names=["post"]
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        refresh=RefreshToken.for_user(user)
        res={
            "refresh":str(refresh),
            "access":str(refresh.access_token),
        }
        return Response(
            {
                "user":serializer.data,
                "refresh":res["refresh"],
                "access":res["access"],
            },
            status=status.HTTP_201_CREATED
        )



