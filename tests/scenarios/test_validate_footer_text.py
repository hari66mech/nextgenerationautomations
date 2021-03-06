from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from pageobjectmodel.validate_footer_text import Footer_text

import pytest
from constants.constant import Constant

scenarios(
    "C:/Users/harikrishna.manokara/PycharmProjects/nextgenerationautomation/tests/features/validate_footer.feature")


@pytest.fixture
def driver():
    browser = webdriver.Chrome(Constant.DRIVER_PATH)
    yield browser
    browser.quit()


@given('I am launching chrome browser')
def home(driver):
    driver.get(Constant.HOME_PAGE_URL)


@when("I am scrolling down the page")
def clicking_slide(driver):
    driver.maximize_window()
    driver.execute_script(Footer_text.scroll_down)


@then("show the footer text")
def results(driver):
    footer_text = driver.find_element_by_xpath(Footer_text.footer_text_loc)
    assert footer_text.text == Footer_text.footer_text
