Feature: OrangeHRM login

  Background: Common steps
    Given I Launch Chrome browser
    When I Open orange HRM application
    And Enter valid username and password
    And click to login


  Scenario: Login to OrangeHRM Application
    Then user must login to the Dashboard

  Scenario: Search User
    When navigate to search page
    Then search page should display

  Scenario: Advance user Search
    When navigate to advance search page
    Then advance search page should display