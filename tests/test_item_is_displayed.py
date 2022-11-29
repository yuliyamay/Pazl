import pytest
import time
from pages.login_page import LoginPage
from pages.locators import *

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"

@pytest.mark.TC_004_03
def test_verify_items_added_to_shopping_cart(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.BIKE_LIGHT_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.BOLT_TSHIRT_ADD_TO_CART_BUTTON)
    time.sleep(4)
    shopping_cart = driver.element_is_present(*InventoryPageLocators.SHOPPING_CART)
    assert shopping_cart


