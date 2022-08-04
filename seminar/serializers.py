from rest_framework import serializers
from rest_framework import status

from seminar.models import Seminar, UserSeminar
from user.models import User


class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = (
            'id',
            'name',
            'capacity',
        )

