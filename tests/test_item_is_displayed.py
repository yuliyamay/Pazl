import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"


@pytest.mark.TC003_02
def test_footer_item_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    # footer_exist = driver.element_is_present(*InventoryPageLocators.FOOTER_SECTION)
    # assert footer_exist, "footer section is not displayed ."
    footer_robot_image_exist = driver.element_is_present(
        *InventoryPageLocators.TERMS_OF_SERVICE
    )
    assert footer_robot_image_exist, "swag-bot image is not displayed ."


@pytest.mark.TC003_01_L
def test_footer_item_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    footer_exist = driver.element_is_present(*InventoryPageLocators.FOOTER_SECTION)
    assert footer_exist, "footer section is not displayed ."


@pytest.mark.TC001_13
def test_username_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    user_field_exist = driver.element_is_present(*LoginPageLocators.LOGIN_USER)
    assert user_field_exist, "Username is not displayed"


@pytest.mark.TC001_15
def test_login_button_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    login_button_exist = driver.element_is_present(*LoginPageLocators.LOGIN_BTN)
    assert login_button_exist, "Button is not displayed"


@pytest.mark.TC001_16
def test_logo_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    logo_exist = driver.element_is_present(*LoginPageLocators.SWAGLABS_LOGO)
    assert logo_exist, "Logo is not displayed"


@pytest.mark.TC001_17
def test_bot_displayed(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    bot_exist = driver.element_is_present(*LoginPageLocators.BOT)
    assert bot_exist, "Bot is not displayed"


@pytest.mark.TC002_01
def test_burger_menu_displayed(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)

    burger_image_exist = driver.element_is_present(
        *InventoryPageLocators.OPEN_MENU_BUTTON
    )
    assert burger_image_exist, "Burger image is not displayed"


@pytest.mark.TC002_02
def test_logo2_displayed(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    logo_exist = driver.element_is_present(*InventoryPageLocators.APP_LOGO)
    assert logo_exist, "Logo is not displayed"


@pytest.mark.TC002_03
def test_cart_displayed(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    cart_exist = driver.element_is_present(*InventoryPageLocators.SHOPPING_CART)
    assert cart_exist, "Shopping cart image is not displayed"


@pytest.mark.TC_002_04
def test_burger_menu_options_displayed(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.OPEN_MENU_BUTTON)
    all_items_exist = driver.element_is_present(
        *InventoryPageLocators.ALL_ITEMS_MENU_ITEM
    )
    assert all_items_exist, "All items does not exist"
    about_exists = driver.element_is_present(*InventoryPageLocators.ABOUT_MENU_ITEM)
    assert about_exists, "About does not exist"
    logout_exists = driver.element_is_present(*InventoryPageLocators.LOGOUT_MENU_ITEM)
    assert logout_exists, "Logout does not exist"
    reset_app_state_exists = driver.element_is_present(
        *InventoryPageLocators.RESET_APP_STATE
    )
    assert reset_app_state_exists, "Reset app state does not exist"
