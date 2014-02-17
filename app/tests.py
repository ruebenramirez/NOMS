from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class APITests(APITestCase):

  # Orders
  def test_get_orders_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('order-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

  #Products    
  def test_get_product_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('product-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  #Catalogs    
  def test_get_catalog_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('catalog-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

  #Line Items    
  def test_get_lineitem_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('lineitem-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
