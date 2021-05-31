from django.db import models


class Customer(models.Model):
    first_name=models.CharField(blank=False,null=False,max_length=50)
    last_name=models.CharField(blank=False,null=False ,max_length=50)
    phone_number=models.CharField(unique=True,null=False,max_length=15)
    email=models.EmailField(unique=True,null=False)
    password=models.CharField(max_length=500,null=False,blank=False)

    def __str__(self):
        return self.phone_number

    def add_new_customer(self):
        self.save()

    def check_customer(self):
        error_message=None
        if Customer.objects.filter(phone_number=self.phone_number):
            error_message="Phone Number is already registered."
        elif Customer.objects.filter(phone_number=self.phone_number):
            error_message="Email is already registered."
        return error_message

    @staticmethod
    def find_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            return Customer.objects.get(id=int(customer_id))
        except:
            return False
