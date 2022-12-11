import time

from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators
from pages.locators import CheckOutYourInformationPage


class InventoryPage(LoginPage):
    def get_amount_of_items_in_cart(self):
        elem = self.browser.find_element(*InventoryPageLocators.SHOPPING_CART_BADGE)
        text = elem.text
        return text

    def find_elements(self, method, locator):
        sorted_list = []
        for option in self.browser.find_elements(*CartPageLocators.ITEMS_IN_CART):
            sorted_list.append(option.text)
        return sorted_list

    def go_to_cart(self):
        self.click_element(*InventoryPageLocators.SHOPPING_CART)

    def find_items_in_cart(self):
        return self.find_elements(*CartPageLocators.ITEMS_IN_CART)

    def error_first_name_is_required(self):
        element = self.browser.find_element(
            *CheckOutYourInformationPage.ERROR_FIRST_NAME
        )
        text = element.text
        return text

    def error_last_name_is_required(self):
        element = self.browser.find_element(*CheckOutYourInformationPage.ERROR_LAST_NAME)
        text = element.text
        return text

    def error_zipcode_required(self):
        element = self.browser.find_element(*CheckOutYourInformationPage.ERROR_POSTAL_ZIPCODE)
        text = element.text
        return text

