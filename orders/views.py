from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from orders.filters import OrderFilter
from orders.models import Order, OrderHistory
from orders.paginations import OrderPagination
from orders.serializers import OrderSerializer


# Create your views here.

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = OrderFilter

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        OrderHistory.objects.create(order=queryset.first())

