import time
import pytest
from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import FilterOptions
from helper.helpers import count_items
from helper.helpers import make_list
from pages.cart_page import CartPage

from pages.locators import CartPageLocators
import logging

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
def test_check_number_in_cart(browser):
    logging.info(f"test_check_number_in_cart")
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


@pytest.mark.ТC_004_01
@pytest.mark.parametrize(
    "locator_filter,locator_items,reverse_mark, convert_to_number",
    [
        (
            FilterOptions.NAME_A_Z,
            InventoryPageLocators.INVENTORY_NAMES_LIST,
            False,
            False,
        ),
        pytest.param(
            FilterOptions.NAME_Z_A,
            InventoryPageLocators.INVENTORY_NAMES_LIST,
            True,
            False,
            marks=pytest.mark.z_a,
        ),
        pytest.param(
            FilterOptions.PRICE_LOW_TO_HIGH,
            InventoryPageLocators.INVENTORY_PRICE_LIST,
            False,
            True,
            marks=pytest.mark.l_h,
            id="price_l_h",
        ),
        pytest.param(
            FilterOptions.PRICE_HIGH_TO_LOW,
            InventoryPageLocators.INVENTORY_PRICE_LIST,
            True,
            True,
            # marks=[pytest.mark.h_l, pytest.mark.xfail],
            id="price_h_l",
        ),
    ],
)
def test_verify_different_types_of_sorting(
    locator_filter, locator_items, reverse_mark, convert_to_number, browser
):

    driver = InventoryPage(browser, link)
    driver.login_success(browser)

    driver.click_element(*locator_filter)
    items_on_page = make_list(browser.find_elements(*locator_items), numbers=convert_to_number)
    items_filtered = sorted(items_on_page, reverse=reverse_mark)
    assert items_on_page == items_filtered, "Items are not sorted."


@pytest.mark.TC_999_09
def test_verify_button_back_to_product(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)

    driver.click_element(*InventoryPageLocators.BOLT_TSHIRT_ITEM_NAME)
    driver.click_element(*InventoryPageLocators.BTN_BACK_TO_PRODUCT)
    assert link + endpoint == browser.current_url, "wrong url"






