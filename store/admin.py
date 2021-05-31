from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminCategory(ImportExportModelAdmin):
    list_display = ['id','name']


class AdminProduct(ImportExportModelAdmin):
    list_display = ['id','name','price','description','category']


class AdminCustomer(ImportExportModelAdmin):
    list_display = ['id','first_name','last_name','phone_number','email','password']


class AdminOrder(ImportExportModelAdmin):
    list_display = ['id','product','customer','phone_number','address','date','quantity','total_price','status']


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)

