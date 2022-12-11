import time

import pytest
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import CheckOutYourInformationPage
from pages.inventory_page import InventoryPage

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"


@pytest.mark.TC_009_01
def test_check_empty_fields(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    first_name_field = driver.element_is_present(
        *CheckOutYourInformationPage.CHECKOUT_FIRST_NAME
    )
    assert first_name_field, "Field is not empty"
    last_name_field = driver.element_is_present(
        *CheckOutYourInformationPage.CHECKOUT_LAST_NAME
    )
    assert last_name_field, "Field is not empty"
    zipcode_field = driver.element_is_present(
        *CheckOutYourInformationPage.ZIP_CODE_FIELD
    )
    assert zipcode_field, "Field is not empty"


@pytest.mark.TC_009_09
def test_error_first_name_is_required(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_LAST_NAME, "Vice")
    driver.keyboard_input(*CheckOutYourInformationPage.ZIP_CODE_FIELD, "33400")
    driver.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)
    error_text = driver.error_first_name_is_required()
    assert error_text == "Error: First Name is required", "wrong warning text"


@pytest.mark.TC_009_002
def test_redirected_page(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_FIRST_NAME, "John")
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_LAST_NAME, "Smith")
    driver.keyboard_input(*CheckOutYourInformationPage.ZIP_CODE_FIELD, "61007")
    driver.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-two.html")


@pytest.mark.TC_009_003
def test_error_first_name(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_FIRST_NAME, "John")
    driver.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)
    error_text = driver.error_last_name_is_required()
    assert error_text == "Error: Last Name is required", "wrong warning text"


@pytest.mark.TC_009_05
def test_postal_error(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_FIRST_NAME, "John")
    driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_LAST_NAME, "Smith")
    driver.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)
    error_text = driver.error_zipcode_required()
    assert error_text == "Error: Postal Code is required", "wrong warning text"