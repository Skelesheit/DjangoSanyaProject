from rest_framework import serializers

from orders.models import Order, PrintFile, Contact, OrderHistory


class PrintFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintFile
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'
