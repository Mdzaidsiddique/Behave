Feature: OrangeHRM login
  Scenario: Login to Orange HRM with valid credentials
    Given I Launch Chrome browser
    When I Open orange HRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to dashboard page

  Scenario Outline: Login to orange HRM with multiple credentials
    Given I Launch Chrome browser
    When I Open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |

# 02_step_parameter.py is there for this