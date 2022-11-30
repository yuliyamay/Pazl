import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"
invalid_user = "invalid"
invalid_password = "invalid"
locked_out_user = "locked_out_user"


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
    assert error_text == "Epic sadface: Password is required", "wrong warning text"


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
        "match any user in this service"
    ), "wrong warning text"


@pytest.mark.TC001_03
def test_login_empty_fields(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert error_text == "Epic sadface: Username is required", "wrong warning text"


@pytest.mark.TC001_19
def test_hidden_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    pas_locator = "//div/input[@type='password']"
    assert (
        browser.find_element(By.XPATH, pas_locator).get_attribute('type') == "password"
    ), "Password is not hidden"


@pytest.mark.TC001_21_01
def test_user_is_redirected_to_inventory_page_standard_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.xfail
def test_user_is_redirected_to_inventory_page_locked_out_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(locked_out_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.TC001_21_05
def test_login_locked_out_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(locked_out_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text == 'Epic sadface: Sorry, this user has been locked out.'
    ), "wrong warning text"
