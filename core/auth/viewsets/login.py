from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ..serializers.login import LoginSerilizer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class LoginViewSet(ViewSet):

    serializer_class=LoginSerilizer
    http_method_names=["post"]


    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={"request":request})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
            
        

