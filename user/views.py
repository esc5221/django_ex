from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import serializers, status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from user.serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.GenericViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=False)
    def participant(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request):
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data='유저가 존재하지 않습니다.')

        return Response(self.get_serializer(user).data)
