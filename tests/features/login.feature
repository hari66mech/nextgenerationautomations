Feature: Next generation automation login

    Scenario: Verify the user login with valid credential
        Given I am launching chrome browser
        When Login as the valid credential
        Then Redirect to the home page