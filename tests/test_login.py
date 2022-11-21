import pytest
from pages.login_page import LoginPage
link = "https://www.saucedemo.com/"


@pytest.mark.smoke
def test_login_valid_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name()
    driver.enter_user_password()
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
def test_login_without_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name()
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text == "Epic sadface: Password is required"
    ), "wrong warning text"
