from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators


class InventoryPage(LoginPage):
    def getting_amount_of_items_in_cart(self):
        elem = self.browser.find_element(*InventoryPageLocators.SHOPPING_CART_BADGE)
        text = elem.text
        return text
