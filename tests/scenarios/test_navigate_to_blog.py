from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pytest
from constants.constant import Constant
from pageobjectmodel.navigate_to_blog_locators import Navigation
from selenium.webdriver.support import expected_conditions as EC
import time

scenarios(
    "C:/Users/harikrishna.manokara/PycharmProjects/nextgenerationautomation/tests/features/navigate_to_blog.feature")


@pytest.fixture
def driver():
    browser = webdriver.Chrome(Constant.DRIVER_PATH)
    yield browser
    browser.quit()


@given('I am launching chrome browser')
def home(driver):
    driver.get(Constant.HOME_PAGE_URL)


@when("I am clicking the slide")
def clicking_slide(driver):
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, Navigation.navigation_button_loc)))
    login_button.click()


@then("Redirect to the another page")
def results(driver):
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
    assert driver.current_url != "https://www.nextgenerationautomation.com/"
