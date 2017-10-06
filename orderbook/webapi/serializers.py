from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ( 'id', 'name', 'contact', 'address')


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'type', 'firm', 'description', 'order_date', 'total', 'status', 'payment', 'customer')

class PendingOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'type', 'firm', 'status')

class DuePaymentOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'type', 'firm', 'due')
