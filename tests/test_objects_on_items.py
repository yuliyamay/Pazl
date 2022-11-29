import pytest
from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"


@pytest.mark.TC_007_01
def test_verify_objects(browser):
    driver = InventoryPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    driver.click_element(*InventoryPageLocators.BACKPACK_ITEM_IMAGE)
    backpack_image_exists = driver.element_is_present(*InventoryPageLocators.BACKPACK_ITEM_IMAGE)
    assert backpack_image_exists, "Backpack image is not displayed"  # works
    backpack_name_exists = driver.element_is_present(*InventoryPageLocators.BACKPACK_ITEM_NAME)
    assert backpack_name_exists, "Backpack name is not displayed"  # works
    backpack_description_exists = driver.element_is_present(*InventoryPageLocators.BACKPACK_PRODUCT_DESCRIPTION)
    assert backpack_description_exists, "Backpack description is not displayed"  # works
    backpack_price_exists = driver.element_is_present(*InventoryPageLocators.BACKPACK_PRICE)
    assert backpack_price_exists, "Backpack price is not displayed"  # works
    backpack_add_to_cart = driver.element_is_present(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    assert backpack_add_to_cart, "Backpack add to cart is not displayed"  # works
    back_to_product_button_exists = driver.element_is_present(*InventoryPageLocators.BACKPACK_BACK_BUTTON)
    assert back_to_product_button_exists, "Back button is not displayed"
