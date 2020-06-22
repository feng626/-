from rest_framework import serializers

from common.serializers import ModelSerializer
from . import models


class FractionSerializer(ModelSerializer):
    user_name = serializers.CharField(help_text='用户名称', source='user.username', read_only=True)

    class Meta:
        model = models.Fraction
        fields = (
            "id",
            "value",
            "user",
            "user_name",
        )


class FractionModifySerializer(serializers.Serializer):
    value = serializers.IntegerField(help_text='分数')
