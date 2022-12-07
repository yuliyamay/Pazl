import time

import pytest
from pages.cart_page import CartPage
from pages.locators import CartPageLocators
from pages.locators import FirstItemPageLocators
from helper.helpers import make_list
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/cart.html"


@pytest.mark.TC_006_08
def test_item_data_displayed(browser):
    driver = CartPage(browser, link)
    driver.login_success(browser)
    driver.item_in_cart(browser)
    qty_displayed = driver.element_is_present(*CartPageLocators.QTY_BOX)
    assert qty_displayed, "Quantity (QTY) is not displayed."
    name_displayed = driver.element_is_present(*CartPageLocators.NAME_BACKPACK_CART)
    assert name_displayed, "Name is not displayed."
    description_displayed = driver.element_is_present(
        *CartPageLocators.DESCRIPTION_ITEM_CART
    )
    assert description_displayed, "Description is not displayed."
    price_displayed = driver.element_is_present(*CartPageLocators.PRICE_ITEM_CART)
    assert price_displayed, "Price is not displayed."
    driver.click_element(*FirstItemPageLocators.REMOVE_BUTTON_FIRST_ITEM)


@pytest.mark.TC_007_02_L
def test_verify_user_can_add_product_to_cart_L(browser):
    driver = CartPage(browser, link)
    driver.login_success(browser)

    amount_displayed = driver.element_is_present(
        *InventoryPageLocators.SHOPPING_CART_BADGE
    )
    assert amount_displayed == False, "Number in cart is not 0."

    driver.item_in_cart(browser)

    items_on_page = make_list(
        driver.find_items_in_cart(), item_name="Sauce Labs Backpack"
    )
    assert items_on_page, "Item is not in the cart."

    amount = driver.get_amount_of_items_in_cart()
    assert (
        int(amount) == 1
    ), "Number of products in the cart (the Primary Header) is not increased."

    driver.click_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")

    add_btn_present = driver.element_is_present(
        *InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON
    )
    assert (
        add_btn_present == False
    ), "Button has not turned into the “Remove” button after that."
    driver.element_is_present(*InventoryPageLocators.BACKPACK_REMOVE_BUTTON)
