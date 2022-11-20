import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://www.saucedemo.com'


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    browser.quit()


class TestLoginPage():

    @pytest.mark.login
    def test_password_empty_error(self, browser):

        browser.get(BASE_URL)
        browser.find_element(By.ID, 'user-name').send_keys('invalid')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()
        error_locator = "h3[data-test='error']"
        assert browser.find_element(By.CSS_SELECTOR, error_locator).text == 'Epic sadface: Username and password do not match any user in this service'
