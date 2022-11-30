from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators

link = "https://www.saucedemo.com/"

class CartPage(LoginPage):
    def item_in_cart(self):
        self.login_success()
        self.click_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART_BUTTON)
        self.click_element(*InventoryPageLocators.SHOPPING_CART)
        self.should_be_current_page('https://www.saucedemo.com/cart.html')
