from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb


def test_1():
    browser = webdriver.Chrome()
    print('browser', browser)
    browser.get("https://wiki.ubuntu.com")
    element = browser.find_elements(By.ID, "searchinput")
    # element.send_keys("typing")
    print('****************************')
    print(element)
    # pdb.set_trace()
    print('****************************')
    time.sleep(3)
    browser.close()