import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

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
        time.sleep(1)
        items += 1
        print(items)

        amount = driver.getting_amount_of_items_in_cart()

        assert int(amount) == items, "Wrong number in the cart. +"

    print("****** ------- ***********")

    while driver.element_is_present(*InventoryPageLocators.BUTTONS_REMOVE_X):
        driver.click_element(*InventoryPageLocators.BUTTONS_REMOVE_X)
        time.sleep(1)
        items -= 1
        print(items)

        if items == 0:
            assert amount_displayed == False, "Number in cart is not 0. -"
        else:
            amount = driver.getting_amount_of_items_in_cart()
            assert int(amount) == items, "Wrong number in the cart. -"
