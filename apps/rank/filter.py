from django_filters import rest_framework as filters

from .models import Fraction


class FractionFilter(filters.FilterSet):
    user_id = filters.CharFilter(field_name="user_id")

    class Meta:
        model = Fraction
        fields = ['user_id']
