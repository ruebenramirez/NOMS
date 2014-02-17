from rest_framework import viewsets
from app.models import Order, LineItem, Catalog, Product
from app.serializers import OrderSerializer, LineItemSerializer, CatalogSerializer, ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LineItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows list items to be viewed or edited.
    """
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer

class CatalogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows catalogues to be viewed or edited.
    """
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
