import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser...')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.saucedemo.com')
    yield browser
    print('\nquit browser...')
    browser.quit()
