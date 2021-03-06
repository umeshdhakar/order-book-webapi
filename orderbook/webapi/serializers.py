from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ( 'id', 'name', 'contact_1', 'contact_2', 'address')


class CustomerListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id','name')


class OrderSerializers(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'type', 'customer', 'firm', 'description', 'order_date', 'delivery_date', 'total', 'discount', 'advance', 'due', 'status', 'payment')


class NewOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'type', 'customer', 'firm', 'description', 'order_date', 'total', 'discount', 'advance', 'due', 'status', 'payment')


class PendingOrderSerializers(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'type', 'firm', 'status', 'customer')

class DuePaymentOrderSerializers(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.name', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'type', 'firm', 'due', 'customer')
