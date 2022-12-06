import time

from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators
from pages.locators import CartPageLocators


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
