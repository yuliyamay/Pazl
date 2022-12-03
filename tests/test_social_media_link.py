import pytest
import time

from pages.inventory_page import InventoryPage
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"



@pytest.mark.TC_002_05
def test_about_link(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.OPEN_MENU_BUTTON)
    time.sleep(1)
    driver.click_element(*InventoryPageLocators.ABOUT_MENU_ITEM)
    driver.should_be_current_page("https://saucelabs.com/")
