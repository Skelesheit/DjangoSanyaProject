# orders/filters.py
import django_filters
from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    material = django_filters.CharFilter(lookup_expr='exact')
    quality = django_filters.CharFilter(lookup_expr='exact')
    created_at__gte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['material', 'quality', 'created_at']
