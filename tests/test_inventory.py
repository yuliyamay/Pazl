import time
import pytest
from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators
from helper.helpers import count_items
from pages.locators import CartPageLocators
import pdb

link = "https://www.saucedemo.com/"
endpoint = "inventory.html"

regular_user = "standard_user"
password = "secret_sauce"


@pytest.mark.TC_004_02_L
def test_check_number_in_cart(browser):
    driver = InventoryPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")

    cart_displayed = driver.element_is_present(*InventoryPageLocators.SHOPPING_CART)
    assert cart_displayed, "Cart is not displayed."

    print("****** +++++++ ***********")

    amount_displayed = driver.element_is_present(
        *InventoryPageLocators.SHOPPING_CART_BADGE
    )
    assert amount_displayed == False, "Number in cart is not 0."

    items = 0
    amount = 0
    while driver.element_is_present(*InventoryPageLocators.BUTTONS_ADD_X):
        driver.click_element(*InventoryPageLocators.BUTTONS_ADD_X)
        items += 1
        print(items)

        amount = driver.getting_amount_of_items_in_cart()

        assert int(amount) == items, "Wrong number in the cart. +"

    print("****** ------- ***********")

    while driver.element_is_present(*InventoryPageLocators.BUTTONS_REMOVE_X):
        driver.click_element(*InventoryPageLocators.BUTTONS_REMOVE_X)
        items -= 1
        print(items)

        if items == 0:
            assert amount_displayed == False, "Number in cart is not 0. -"
        else:
            amount = driver.getting_amount_of_items_in_cart()
            assert int(amount) == items, "Wrong number in the cart. -"


@pytest.mark.TC_004_04_L
def test_check_number_in_cart1(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)

    driver.element_is_present(*InventoryPageLocators.BACKPACK_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)

    driver.element_is_present(*InventoryPageLocators.FLEECE_JACKET_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.FLEECE_JACKET_ADD_TO_CART_BUTTON)

    driver.element_is_present(*InventoryPageLocators.RED_SHIRT_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.RED_SHIRT_ADD_TO_CART_BUTTON)

    driver.go_to_cart()
    items_in_cart = count_items(driver.find_items_in_cart())
    assert items_in_cart == 3, "Should be three items in cart."

    driver.element_is_present(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
    driver.click_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)

    assert link + endpoint == browser.current_url, "wrong url"

    driver.element_is_present(*InventoryPageLocators.BACKPACK_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.BACKPACK_REMOVE_BUTTON)

    driver.element_is_present(*InventoryPageLocators.FLEECE_JACKET_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.FLEECE_JACKET_REMOVE_BUTTON)

    driver.element_is_present(*InventoryPageLocators.RED_SHIRT_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.RED_SHIRT_REMOVE_BUTTON)

    driver.go_to_cart()
    items_in_cart = count_items(driver.find_items_in_cart())
    assert items_in_cart == 0, "Should be None items in cart."
