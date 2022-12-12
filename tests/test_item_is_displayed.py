import time

import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.locators import LoginPageLocators, CheckOutOverviewPage, CheckOutCompletePage
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import CheckOutYourInformationPage
from selenium.webdriver.common.by import By
from pages.footer_section import FooterSection
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

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
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.BIKE_LIGHT_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.BOLT_TSHIRT_ADD_TO_CART_BUTTON)
    time.sleep(4)
    shopping_cart = driver.element_is_present(*InventoryPageLocators.SHOPPING_CART)
    assert shopping_cart

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


@pytest.mark.ТC_004_01L
def test_filter_is_present(browser):
    driver = InventoryPage(browser, link)
    driver.login_success(browser)
    filter_is_present = driver.element_is_present(
        *InventoryPageLocators.PRODUCT_SORT_FILTER
    )
    assert filter_is_present, "Filter button is not displayed"


@pytest.mark.TC_002_06
def test_header_displayed(browser):
    driver = InventoryPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")
    driver.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    header_cart_page_displayed = driver.element_is_present(
        *CartPageLocators.SECONDARY_HEADER
    )
    assert header_cart_page_displayed, "Header is not displayed"
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    header_checkout_displayed = driver.element_is_present(
        *CheckOutYourInformationPage.PRIMARY_HEADER
    )
    assert header_checkout_displayed, "Header is not displayed"
    # driver.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_FIRST_NAME, "John") (Other way)
    driver.keyboard_input(By.CSS_SELECTOR, "#first-name", "John")
    driver.keyboard_input(By.CSS_SELECTOR, "#last-name", "Smith")
    driver.keyboard_input(By.CSS_SELECTOR, "#postal-code", "61007")
    time.sleep(1)
    driver.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-two.html")
    header_overview_page = driver.element_is_present(
        *CheckOutOverviewPage.HEADER_OVERVIEW
    )
    assert header_overview_page, "Header is not displayed"
    driver.click_element(*CheckOutOverviewPage.FINISH_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-complete.html")
    header_checkout_complete_page = driver.element_is_present(
        *CheckOutCompletePage.HEADER_COMPLETE_PAGE
    )
    assert header_checkout_complete_page, "Header is not displayed"


@pytest.mark.TC_009_10
def test_first_name_field_exists(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    first_name_field = driver.element_is_present(
        *CheckOutYourInformationPage.CHECKOUT_FIRST_NAME
    )
    assert first_name_field, "First name field is not displayed"


@pytest.mark.TC_009_11
def test_last_name_field_exists(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    last_name_field = driver.element_is_present(
        *CheckOutYourInformationPage.CHECKOUT_LAST_NAME
    )
    assert last_name_field, "Last name field is not displayed"


@pytest.mark.TC_009_12
def test_zipcode_field_exists(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    zipcode_field = driver.element_is_present(
        *CheckOutYourInformationPage.ZIP_CODE_FIELD
    )
    assert zipcode_field, "Zipcode field field does not exist"


@pytest.mark.TC_009_13
def test_cancel_button_exists(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    cancel_button = driver.element_is_present(
        *CheckOutYourInformationPage.CANCEL_BUTTON
    )
    assert cancel_button, "Cancel button is not displayed"


@pytest.mark.TC_009_14
def test_cancel_button_exists(browser):
    driver = LoginPage(browser, link)
    driver.login_success(browser)
    driver.click_element(*InventoryPageLocators.SHOPPING_CART)
    driver.should_be_current_page("https://www.saucedemo.com/cart.html")
    driver.click_element(*CartPageLocators.CHECKOUT_BUTTON)
    driver.should_be_current_page("https://www.saucedemo.com/checkout-step-one.html")
    continue_button = driver.element_is_present(
        *CheckOutYourInformationPage.CONTINUE_BUTTON
    )
    assert continue_button, "Continue button is not displayed"


@pytest.mark.TC_003_02
def test_footer_displayed_navigation_flow_pages(browser):
    driver_footer = FooterSection(browser, link)
    driver_footer.login_success(browser)
    driver_footer.footer_is_displayed()

    driver = CartPage(browser, link)
    driver.item_in_cart(browser)
    driver_footer.footer_is_displayed()

    driver = CheckoutPage(browser, link)
    driver.check_out_your_information()
    driver_footer.footer_is_displayed()

    driver.input_first_name()
    driver.input_last_name()
    driver.input_zip_code()
    driver.click_button_continue()
    driver_footer.footer_is_displayed()

    driver.checkout()
    driver_footer.footer_is_displayed()
