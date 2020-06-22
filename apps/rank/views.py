from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import mixins

from . import serializers
from common.view import BaseGenericViewSet
from . import models
from . import filter


class FractionViewSet(BaseGenericViewSet, mixins.ListModelMixin):
    queryset = models.Fraction.objects.select_related('user')
    serializers_module = serializers
    filterset_class = filter.FractionFilter

    def list(self, request, *args, **kwargs):
        response = super(FractionViewSet, self).list(request, *args, **kwargs)
        results = response.data['results']
        offset = int(request.query_params['offset'][0])
        for index, result in enumerate(results, start=1):
            result['rank'] = offset + index
        user = request.user
        for index, instance in enumerate(self.queryset.order_by('-value'), start=1):
            if instance.user_id == user.id:
                results.append({'id': instance.id, 'value': instance.value, 'user': user.id,
                                'user_name': user.username, 'rank': index})
                break
        return response

    @action(methods=["patch"], detail=False)
    def modify(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        value = serializer.data.get('value')
        instance = models.Fraction.objects.get(user=request.user)
        instance.value = value
        instance.save()
        return Response({}, status=status.HTTP_200_OK)
