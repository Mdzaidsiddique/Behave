Feature: Google homepage logo validation
  Scenario: Logo presence on google home page
    Given launch Chrome browser
    When open google home page
    Then verify that the logo present on page
    And close the browser