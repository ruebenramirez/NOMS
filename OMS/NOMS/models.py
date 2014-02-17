from django.db import models

class Order(models.Model):
    created             = models.DateTimeField(auto_now_add=True) 
    customer_approved   = models.BooleanField()
    seller_approved     = models.BooleanField()
    is_paid             = models.BooleanField()

class LineItem(models.Model):
    quantity            = models.IntegerField()
    order               = models.ForeignKey(Order, related_name='lineItems')

class Customer(models.Model):
    order               = models.ForeignKey(Order, related_name='customer')
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    phone_number        = models.CharField(max_length=30)
    email               = models.EmailField()

class Vendor(models.Model):
    line_item           = models.ForeignKey(Order, related_name='vendor')
    business_name       = models.CharField()
    email               = models.EmailField()

class Product(models.Model):
    line_item           = models.ForeignKey(LineItem, related_name='product')
    name                = models.CharField(max_length=30)

# class ProductAttribute(models.Model):
#     product             = models.Foreignkey(Product, related_name='product_attributes')  
#     name                = models.CharField(max_length=30)
#     value               = models.CharField(max_length=30)
