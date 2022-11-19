import pytest
from selenium.webdriver.common.by import By

test_params = (
    pytest.param(
        '//option[text()="Name (A to Z)"]',
        '.inventory_item_name',
        False,
        id='sort_A_Z__param_1'
    ),
    pytest.param(
        '//option[text()="Name (Z to A)"]',
        '.inventory_item_name',
        True,
        id='sort_Z_A__param_2'
    ),
    pytest.param(
        '//option[text()="Price (low to high)"]',
        '.inventory_item_price',
        False,
        id='sort_price_low_to_high__param_3'
    ),
    pytest.param(
        '//option[text()="Price (high to low)"]',
        '.inventory_item_price',
        True,
        id='sort_price_high_to_low__param_4'
    ),
)


@pytest.mark.parametrize("sort_locator, items_locator, reverse_flag", test_params)
def test_sorting_items(sort_locator, items_locator, reverse_flag, browser):
    user_name = browser.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')

    password = browser.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')

    button_login = browser.find_element(By.NAME, 'login-button')
    button_login.click()

    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', "We reach!"
    list_of_product_elements = browser.find_elements(By.CSS_SELECTOR, items_locator)
    products_code_sort = []
    for item in list_of_product_elements:
        products_code_sort.append(item.text)
    product_sort_container = browser.find_element(By.XPATH, '//select[@class="product_sort_container"]')
    product_sort_container.click()
    dropdawn_sorting = browser.find_element(By.XPATH, sort_locator)
    dropdawn_sorting.click()
    list_of_product_elements_after_page_sort = browser.find_elements(By.CSS_SELECTOR, items_locator)
    products_after_page_sort = []
    for product in list_of_product_elements_after_page_sort:
        products_after_page_sort.append(product.text)
    if items_locator == ".inventory_item_price":
        products_after_page_sort = [x.replace('$', '') for x in products_after_page_sort]
        products_after_page_sort = [float(x) for x in products_after_page_sort]
        products_code_sort = [x.replace('$', '') for x in products_code_sort]
        products_code_sort = [float(x) for x in products_code_sort]
    products_code_sort.sort(reverse=reverse_flag)
    print("1")
    assert products_code_sort == products_after_page_sort, "Products are not sorted!"
