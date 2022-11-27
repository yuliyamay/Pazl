import pytest
import time
from pages.login_page import LoginPage
from pages.locators import *

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"
invalid_user = "invalid"
invalid_password = "invalid"


@pytest.mark.smoke
def test_login_valid_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
def test_login_without_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
            error_text == "Epic sadface: Password is required"
    ), "wrong warning text"


@pytest.mark.TC001_01
def test_login_invalid_username(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(invalid_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
            error_text == "Epic sadface: Username and password do not "
                          "match any user in this service"), "wrong warning text"


@pytest.mark.TC001_03
def test_login_empty_fields(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
            error_text == "Epic sadface: Username is required"
    ), "wrong warning text"


# empty username and valid password
@pytest.mark.TC001_04
def test_login_empty_username_L(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_password(password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
            error_text == "Epic sadface: Username is required"
    ), "wrong warning text"








