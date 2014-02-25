from rest_framework import serializers
from app.models import Order, LineItem, Catalog, Product


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ('order', 'product', 'created', 'name', 'quantity', 'value')

class OrderSerializer(serializers.ModelSerializer):
    lineItems = LineItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('created', 'vendor', 'customer', 'lineItems')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('created', 'name', 'quantity')

class CatalogSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Catalog
        fields = ('created', 'name', 'products')

