Feature: daraz testing

Scenario: Verify that product cart properly
    Given Go to Website
    When Check that search option is displayed
    Then Click on search option
    When Input any product name
    Then Check that search icon is displayed
    When Click on search icon
    Then Check that Lenovo laptop is displayed
    When Click on Lenovo laptop
    Then Check that add to cart button is displayed
    When Click on add to cart button
    Then Check that go to cart button is displayed
    When Click on go to cart button
    Then Check that proceed to checkout button is displayed
    When Click on proceed to checkout button

Scenario: Verify that login properly
    Given Go to Website
    When Check that login option is displayed
    Then Click on Login option
    When Input Email
    Then Input Password
    When Check that Login option is displayed
    Then Click on Login option
    