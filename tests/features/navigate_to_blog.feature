Feature: Navigation for next generation automation

    Scenario: Verify the user navigate to another page, by clicking the slide
        Given I am launching chrome browser
        When I am clicking the slide
        Then Redirect to the another page