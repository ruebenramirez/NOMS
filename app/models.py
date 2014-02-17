from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Catalog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()

    class Meta:
        ordering = ('created',)

class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    quantity = models.IntegerField()
    catalog = models.ForeignKey(Catalog)

    class Meta:
        ordering = ('created',)

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    vendor = models.TextField()
    customer = models.TextField()
    products = models.ManyToManyField(Product, through='LineItem')

    class Meta:
        ordering = ('created',)

class LineItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField();
    quantity = models.IntegerField()
    value = models.TextField();

    class Meta:
        ordering = ('created',)
    
