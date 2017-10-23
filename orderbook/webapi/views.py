from django.shortcuts import render
from .models import Order, Customer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializers, DuePaymentOrderSerializers, PendingOrderSerializers, CustomerSerializers, NewOrderSerializers, CustomerListSerializers
from django.db.models import Q
# Create your views here.

class CustomerDetail(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializers

class NewCustomer(generics.CreateAPIView):
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
    queryset = Order.objects.filter(Q(status='pending') | Q(status='progress')).order_by('-id') 
    serializer_class = PendingOrderSerializers

class DuePaymentOrderList(generics.ListAPIView):
    queryset = Order.objects.filter(payment='due').order_by('-id') 
    serializer_class = DuePaymentOrderSerializers

class CustomerOrderList(generics.ListAPIView):
        # queryset = Order.objects.filter(customer__id=self.kwargs['pk'])
        serializer_class = OrderSerializers

        def get_queryset(self):
            pk = self.kwargs['pk']
            orders = Order.objects.filter(customer__id=pk).order_by('-id') 
            return orders
