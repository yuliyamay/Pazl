import pytest
import time
from pages.login_page import LoginPage
from pages.locators import *
link = "https://www.saucedemo.com/"

regular_user = "standard_user"
password = "secret_sauce"
invalid_user = "invalid"
invalid_password = "invalid"


@pytest.mark.smoke
def test_login_valid_user(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")


@pytest.mark.regression
def test_login_without_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text == "Epic sadface: Password is required"
    ), "wrong warning text"


@pytest.mark.TC001_01
def test_login_invalid_username(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(invalid_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text == "Epic sadface: Username and password do not "
                      "match any user in this service"), "wrong warning text"


@pytest.mark.TC001_03
def test_login_empty_fields(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text == "Epic sadface: Username is required"
    ), "wrong warning text"


@pytest.mark.TC_001_10
def test_fourth_item_back_to_product(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    driver.click_element(*InventoryPageLocators.FLEECE_JACKET_ITEM_NAME)
    driver.click_element(*FourthItemPageLocators.BACK_TO_PRODUCTS_BUTTON_FOURTH_ITEM)
    driver.should_be_current_page("https://www.saucedemo.com/inventory.html")

@pytest.mark.TC_003_05
# @pytest.mark.xfail
def test_open_facebook_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    # print("Parent Handle: " + parentHandle)
    driver.click_element(*InventoryPageLocators.FACEBOOK_IMAGE_LINK)
    handles = browser.window_handles
    # print("List of handles: ", handles)
    # time.sleep(3)
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://www.facebook.com/saucelabs")


@pytest.mark.TC_001_02
def test_login_with_invalid_password(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(invalid_password)
    driver.click_login_button()
    error_text = driver.getting_error_text()
    assert (
        error_text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "wrong warning text"

    fileName = str(round(time.time() * 1000)) + ".png"
    destinationFileName = "C:\\Users\\alexa\\Desktop\\screenshots\\"
    destinationFile = destinationFileName + fileName

    try:
        browser.save_screenshot(destinationFile)
        print("Screenshot saved to directory --> :: " + destinationFile)
    except NotADirectoryError:
        print("Not a directory issue")


@pytest.mark.TC_001_14
def test_password_field_exists(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    # password_field = driver.element_is_present(*LoginPageLocators.LOGIN_PASSWORD)
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    if password_field is not None:
        print("element is displayed")


@pytest.mark.TC_003_04
def test_open_facebook_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    driver.click_element(*InventoryPageLocators.TWITTER_IMAGE_LINK)
    handles = browser.window_handles
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://twitter.com/saucelabs")


@pytest.mark.TC_003_06
def test_open_facebook_page(browser):
    driver = LoginPage(browser, link)
    driver.open_main_page()
    driver.enter_user_name(regular_user)
    driver.enter_user_password(password)
    driver.click_login_button()
    parentHandle = browser.current_window_handle
    driver.click_element(*InventoryPageLocators.LINKEDIN_IMAGE_LINK)
    handles = browser.window_handles
    for handle in handles:
        if handle not in parentHandle:
            browser.switch_to.window(handle)
    driver.should_be_current_page("https://www.linkedin.com/company/sauce-labs/")

