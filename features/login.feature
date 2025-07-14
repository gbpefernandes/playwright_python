Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I log in with valid credentials
    Then I should see the Welcome page
