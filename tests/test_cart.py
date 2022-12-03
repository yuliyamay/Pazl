import pytest
from pages.cart_page import CartPage
from pages.locators import CartPageLocators
from pages.locators import FirstItemPageLocators

link = "https://www.saucedemo.com/cart.html"


@pytest.mark.TC_006_08
def test_item_data_displayed(browser):
    driver = CartPage(browser, link)
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
