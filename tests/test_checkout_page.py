import pytest
from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import CheckOutYourInformationPage

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
