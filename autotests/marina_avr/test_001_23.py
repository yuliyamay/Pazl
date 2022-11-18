import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://www.saucedemo.com'

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    print('\nquit browser...')
    browser.quit()

class TestLoginPage():

    @pytest.mark.login
    def test_password_empty_error(self, browser):
        browser.get(BASE_URL)
        username = browser.find_element(By.ID, 'user-name')
        username.send_keys('standard_user')
        button_login = browser.find_element(By.NAME, 'login-button').click()
        error_locator = '//*[@id="login_button_container"]/div/form/div[3]/h3'
        assert browser.find_element(By.XPATH, error_locator).text == 'Epic sadface: Password is required'



