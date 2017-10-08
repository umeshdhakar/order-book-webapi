from django.shortcuts import render
from .models import Order, Customer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializers, DuePaymentOrderSerializers, PendingOrderSerializers, CustomerSerializers, NewOrderSerializers
# Create your views here.

class CustomerDetail(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class OrderDetail(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class NewOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = NewOrderSerializers
    # permission_classes = (IsAuthenticated,)

class PendingOrderList(generics.ListAPIView):
    queryset = Order.objects.filter(status='pending')
    serializer_class = PendingOrderSerializers

class DuePaymentOrderList(generics.ListAPIView):
    queryset = Order.objects.filter(payment='due')
    serializer_class = DuePaymentOrderSerializers

class CustomerOrderList(generics.ListAPIView):
        queryset = Order.objects.filter(customer__id=2)
        serializer_class = OrderSerializers
