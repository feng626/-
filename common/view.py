from django.urls import reverse
from rest_framework import viewsets
from rest_framework.test import APITestCase

from common.mixins.views import GenericMixin


class BaseGenericViewSet(GenericMixin, viewsets.GenericViewSet):
    """
    推荐使用的
    """


class BaseAPITestCase(APITestCase):
    basename = ''
    args = ('v1',)

    def setUp(self, ) -> None:
        response = self.client.login(username='test', password='test')
        self.assertTrue(response)
        self.path = reverse(self.basename, args=self.args)
