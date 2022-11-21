
from pages.base_page import BasePage
from pages.locators import LoginPageLocators

link = "https://www.saucedemo.com/"

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


