from rest_framework import serializers, status, viewsets, permissions
from rest_framework.response import Response

from seminar.models import Seminar
from seminar.serializers import SeminarSerializer


class SeminarViewSet(viewsets.GenericViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    permission_classes = (permissions.IsAuthenticated(),)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return (permissions.AllowAny(),)
        return self.permission_classes

    def list(self, request):
        seminars = Seminar.objects.all()
        return Response(self.get_serializer(seminars, many=True).data)

    def retrieve(self, request, pk=None):
        try:
            seminar = Seminar.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND, data='세미나가 존재하지 않습니다.')

        return Response(self.get_serializer(seminar).data)

    def create(self, request):
        return Response(status=status.HTTP_201_CREATED)
