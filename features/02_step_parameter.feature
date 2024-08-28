Feature: OrangeHRM login
  Scenario: Login to Orange HRM with valid credentials
    Given I Launch Chrome browser
    When I Open orange HRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to dashboard page
