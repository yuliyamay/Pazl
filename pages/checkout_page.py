from pages.cart_page import CartPage
from pages.locators import CartPageLocators
from pages.locators import CheckOutYourInformationPage


class CheckoutPage(CartPage):

    def check_out_your_information(self):
        self.click_element(*CartPageLocators.CHECKOUT_BUTTON)

    def input_first_name(self):
        self.keyboard_input(*CheckOutYourInformationPage.CHECKOUT_FIRST_NAME, ' FIRST NAME')

    def input_last_name(self):
        pass

    def input_zip_code(self):
        self.keyboard_input(*CheckOutYourInformationPage.ZIP_CODE_FIELD, 'POSTAL CODE')

    def click_button_continue(self):
        self.click_element(*CheckOutYourInformationPage.CONTINUE_BUTTON)




