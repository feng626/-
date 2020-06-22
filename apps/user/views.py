from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import mixins

from . import serializers
from .exceptions import UserNameError, PasswordError
from common.view import BaseGenericViewSet
from . import models


class UserViewSet(BaseGenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = models.User.objects.all()
    serializers_module = serializers

    _ignore_model_permissions = True

    @action(methods=["post"], detail=False)
    def login(self, request: Request, *args, **kwargs):
        user = authenticate(request,
                            username=request.data.get('username'),
                            password=request.data.get('password'))

        if not user:
            if models.User.objects.filter(username=request.data.get('username')).exists():
                raise PasswordError()
            else:
                raise UserNameError()
        login(request, user)
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
