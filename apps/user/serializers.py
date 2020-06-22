from django.db.transaction import atomic
from rest_framework import serializers

from common.serializers import ModelSerializer
from . import models
from rank.models import Fraction


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'password')


class UserSerializer(ModelSerializer):
    password = serializers.CharField(required=False, write_only=True,
                                     allow_blank=True)

    class Meta:
        model = models.User
        fields = (
            "id",
            "no",
            "username",
            "password",
            "email",
        )

    @atomic
    def create(self, validated_data):
        self.pre_create(validated_data)
        user = models.User.objects.create(**validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        user.save()

        Fraction.objects.create(value=0, user=user)
        return user
