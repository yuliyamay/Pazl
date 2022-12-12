from pages.login_page import LoginPage
from pages.locators import InventoryPageLocators


class FooterSection(LoginPage):

    def footer_is_displayed(self):
        footer_exist = self.browser.find_element(*InventoryPageLocators.FOOTER_SECTION)
        url = self.browser.current_url
        assert footer_exist, "\nfooter section is not displayed. Page: " + url