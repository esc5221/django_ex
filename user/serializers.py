from rest_framework import serializers
from rest_framework import status

from seminar.models import Seminar, UserSeminar
from user.models import User

from seminar.serializers import SeminarSerializer


class UserSerializer(serializers.ModelSerializer):
    seminars = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'seminars',
        )

    def get_seminars(self, obj):
        return SeminarSerializer(obj.seminars.all(), many=True).data
