from django.conf.urls import patterns, url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'lineitems', views.LineItemViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'catalogs', views.CatalogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
