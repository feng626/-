from django.db.models import QuerySet
from common.util.seri_util import get_seri


class GenericMixin(object):
    serializers_module = None
    serializer_basename = None

    def get_queryset(self) -> QuerySet:
        qs = super(GenericMixin, self).get_queryset()
        return qs

    def get_serializer_class(self):

        if self.serializers_module is not None:
            _action = self.action

            if self.serializer_basename is not None:
                return get_seri(self.serializer_basename,
                                self.request.method,
                                _action,
                                self.serializers_module)
            else:
                return get_seri(self.__class__.__name__[:-7],  # 删掉 `ViewSet`
                                self.request.method,
                                _action,
                                self.serializers_module)
        else:
            return super(GenericMixin, self).get_serializer_class()
