import time

import pytest
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"


@pytest.mark.TC003_02
def test_footer_item_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    # footer_exist = driver.element_is_present(*InventoryPageLocators.FOOTER_SECTION)
    # assert footer_exist, "footer section is not displayed ."
    footer_robot_image_exist = driver.element_is_present(*InventoryPageLocators.TERMS_OF_SERVICE)
    assert footer_robot_image_exist, "swag-bot image is not displayed ."


@pytest.mark.TC003_01
def test_footer_section_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    footer_exist = driver.element_is_present(*InventoryPageLocators.FOOTER_SECTION)
    assert footer_exist, "footer section is not displayed."


@pytest.mark.TC001_13
def test_username_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    user_field_exist = driver.element_is_present(*LoginPageLocators.LOGIN_USER)
    assert user_field_exist, "Username is not displayed."


@pytest.mark.TC_003_05_L
def test_open_twitter_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.TWITTER_IMAGE_LINK)
    browser.switch_to.window(browser.window_handles[1])
    driver.should_be_current_page("https://twitter.com/saucelabs")