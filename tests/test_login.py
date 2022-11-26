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


@pytest.mark.TC_001_10
def test_fourth_item_back_to_product(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.FLEECE_JACKET_ITEM_NAME)
    driver.click_element(*FourthItemPageLocators.BACK_TO_PRODUCTS_BUTTON_FOURTH_ITEM)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")




@pytest.mark.TC_001_02
def test_login_with_invalid_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(invalid_password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
            error_text
            == "Epic sadface: Username and password do not match any user in this service"
    ), "wrong warning text"

    fileName = str(round(time.time() * 1000)) + ".png"
    destinationFileName = "C:\\Users\\alexa\\Desktop\\screenshots\\"
    destinationFile = destinationFileName + fileName

    try:
        browser.save_screenshot(destinationFile)
        print("Screenshot saved to directory --> :: " + destinationFile)
    except NotADirectoryError:
        print("Not a directory issue")


@pytest.mark.TC_001_14
def test_password_field_exists(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    password_field_exists= driver.element_is_present(*LoginPageLocators.LOGIN_PASSWORD)
    assert password_field_exists, "Password field is not displayed"



@pytest.mark.TC_001_24
def test_username_is_required(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert error_text == 'Epic sadface: Username is required', "wrong warning text"


@pytest.mark.TC_999_12
def test_sixth_item_back_to_product(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.RED_SHIRT_ITEM_NAME)
    # time.sleep(3)
    driver.click_element(*SixthItemPageLocators.BACK_TO_PRODUCTS_BUTTON_SIXTH_ITEM)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.TC_999_11
def test_fifth_item_back_to_product(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.ONESIE_ITEM_NAME)
    # time.sleep(3)
    driver.click_element(*FifthItemPageLocators.BACK_TO_PRODUCTS_BUTTON_FIFTH_ITEM)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.TC_006_04
def test_user_is_redirected_to_inventory_page_from_cart_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*YourCartPage.CONTINUE_SHOPPING_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.TC_009_15
def test_user_is_redirected_to_cart_page_from_check_your_info_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*YourCartPage.CHECKOUT_BUTTON)
    driver.click_element(*CheckOutYourInformationPage.CANCEL_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")


@pytest.mark.TC_001_22
def test_error_message_if_username_field_empty(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_password(password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert error_text == 'Epic sadface: Username is required', "wrong warning text"






