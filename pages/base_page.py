from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    # Open Page
    def open_page(self):
        self.browser.get(self.link)

    # Clicking on the selected item from the locators
    def click_element(self, method, locator):
        self.browser.find_element(method, locator).click()

    # Transmits text or pressing buttons on the keyboard
    def keyboard_input(self, method, locator, keys_text):
        self.browser.find_element(method, locator).send_keys(keys_text)

    # Confirmation of the presence of an element on the page
    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    # Confirmation of the current page address
    def should_be_current_page(self, link):
        assert link in self.browser.current_url, "wrong url"