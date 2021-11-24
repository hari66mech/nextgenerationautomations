import time

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pytest
from constants.constant import Constant
from pageobjectmodel.login_locators import Login
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/nextgenerationautomation/tests/features/login.feature")
fake = Faker(locale='en_IN')


@pytest.fixture
def driver():
    browser = webdriver.Chrome(Constant.DRIVER_PATH)
    yield browser
    browser.quit()


@given('I am launching chrome browser')
def home(driver):
    driver.get(Constant.HOME_PAGE_URL)


@when("Login as the valid credential")
def login(driver):
    driver.maximize_window()
    # time.sleep(10)
    wait = WebDriverWait(driver, 20)
    # login_button = driver.find_element_by_xpath(Login.login_signup_button_loc)
    wait.until(EC.element_to_be_clickable((By.XPATH, Login.login_signup_button_loc)))
    # login_button.click()
    time.sleep(5)
    first_name = driver.find_element_by_xpath(Login.first_name_loc)
    # first_name = wait.until(EC.presence_of_element_located((By.XPATH, Login.first_name_loc)))
    first_name.send_keys(fake.name())
    last_name = driver.find_element_by_xpath(Login.last_name_loc)
    last_name.send_keys(fake.name())
    email = driver.find_element_by_xpath(Login.email_loc)
    email.send_keys(fake.email())
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(fake.password())
    phone_number = driver.find_element_by_xpath(Login.mobile_number_loc)
    phone_number.send_keys(fake.phone_number())
    city = driver.find_element_by_xpath(Login.city_loc)
    city.send_keys(fake.city())
    sign_up = driver.find_element_by_xpath(Login.sign_up)
    sign_up.click()


@then("Redirect to the home page")
def results(driver):
    assert driver.title == "IT Placements Consulting | Next Generation Automation"