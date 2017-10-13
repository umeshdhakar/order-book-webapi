from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    type = models.CharField(max_length=15)
    firm = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    order_date = models.DateField()
    delivery_date = models.DateField(null=True)
    total = models.IntegerField()
    discount = models.IntegerField(null=True)
    advance = models.IntegerField(null=True)
    due = models.IntegerField(null=True)
    status = models.CharField(default='pending', max_length=10, null=True)
    payment = models.CharField(max_length=10, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.type
