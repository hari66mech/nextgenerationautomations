Feature: Validate footer in next generation automation

    Scenario: Verify the user see the footer text, by scrolling down the page
        Given I am launching chrome browser
        When I am scrolling down the page
        Then show the footer text