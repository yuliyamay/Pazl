import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.headless = False
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield browser
    browser.quit()
