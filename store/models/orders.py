import datetime

from django.db import models
from .products import Product
from .customer import Customer


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    phone_number=models.CharField(max_length=15,default='',blank=True)
    address=models.CharField(max_length=200,default='',blank=True)
    status=models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer):
        return Order.objects.filter(customer=customer).order_by('-date')

