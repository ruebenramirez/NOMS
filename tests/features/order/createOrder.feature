Feature: Create Order
  In order to create an order
  As a developer
  I need an api endpoint to submit an order to

  Scenario: Creating an order
    Given I have a valid order
    When I submit the order
    Then I should have created an order

