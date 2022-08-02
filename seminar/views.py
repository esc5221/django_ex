from rest_framework import serializers, status, viewsets, permissions
from rest_framework.response import Response

from seminar.models import Seminar


class SeminarViewSet(viewsets.GenericViewSet):
    queryset = Seminar.objects.all()
    #serializer_class = SeminarSerializer
    permission_classes = (permissions.IsAuthenticated(),)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (permissions.AllowAny(),)
        return self.permission_classes

    def list(self, request):
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_200_OK)

    def create(self, request):
        return Response(status=status.HTTP_201_CREATED)
