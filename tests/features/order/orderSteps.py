from lettuce import *
from rest_framework import status
from rest_framework.test import APITestCase


@before.each_scenario
def setup
  world.api = APITestCase()

#Creating Orders 
@step('I have a valid order')
def valid_order(step):
  world.order = {
      seller: 'seller.id',
      customer: 'customer.id',
      products: [0, 1, 2];
  }
      
@step('I submit the order')
def submit_order(step):
  data = world.order
  response = world.api.client.post('/orders', data, format='json');
  world.api.assertEquals(response.code, 200);
  world.order_id = response.body.id

@step('I should have created an order')
def check_order(step):
  url = '/orders/' + world.order_id
  response = world.api.client.get(url)
  world.api.assertEqual(response.code, 200)

#Creating Orders 
@step('I have a valid updated order')
def valid_updated_order(step):
  #create a valid order
  pass

@step('I submit the updated order')
def submit_updated_order(step):
  #submit the order
  pass

@step('I should have updated the order')
def check_updated_order(step):
  #validate order
  pass
