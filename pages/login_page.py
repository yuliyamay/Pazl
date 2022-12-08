from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.locators import CheckOutYourInformationPage

link = "https://www.saucedemo.com/"
endpoint_inventory = "inventory.html"


class LoginPage(BasePage):
    def open_main_page(self):
        self.open_page()
        self.should_be_current_page(link)

    def enter_user_name(self, username):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, username)

    def enter_user_password(self, password):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.click_element(*LoginPageLocators.LOGIN_BTN)

    def getting_error_text(self):
        elem = self.browser.find_element(*LoginPageLocators.ERROR_WARNING)
        text = elem.text
        return text

    def getting_error_text_checkout_page(self):
        element = self.browser.find_element(
            *CheckOutYourInformationPage.ERROR_FIRST_NAME
        )
        text = element.text
        return text

    def login_success(self, browser):
        self.open_page()
        self.enter_user_name("standard_user")
        self.enter_user_password("secret_sauce")
        self.click_login_button()

        assert link + endpoint_inventory == browser.current_url, "wrong url"
