from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import serializers, status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()

class UserViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    #serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['post'], detail=False)
    def participant(self, request):
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)