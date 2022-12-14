from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_USER = (By.CSS_SELECTOR, "#user-name")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_LIST = (By.CSS_SELECTOR, ".login_credentials_wrap-inner")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_WARNING = (By.XPATH, "//h3[@data-test='error']")
    ERROR_WARNING_1 = (By.CSS_SELECTOR, "h3[data-test]")
    ERROR_ITEM_ON_NAME_FIELD = (By.CSS_SELECTOR, "#user-name + svg")
    ERROR_ITEM_ON_PASSWORD_FIELD = (By.CSS_SELECTOR, "#password + svg")
    ERROR_ELEMENT_BOTTOM_COLOR = (By.CSS_SELECTOR, ".input_error.error")
    SWAGLABS_LOGO = (By.CSS_SELECTOR, ".login_logo")
    BOT = (By.CSS_SELECTOR, ".bot_column")


class InventoryPageLocators:
    # HEADERS
    OPEN_MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    APP_LOGO = (By.CSS_SELECTOR, ".app_logo")
    SHOPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span[class ='shopping_cart_badge'")
    PRIMARY_HEADER = (By.CSS_SELECTOR, "#header_container > div.primary_header")

    INVENTORY_LIST = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_NAMES_LIST = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_PRICE_LIST = (By.CSS_SELECTOR, ".inventory_item_price")

    # BURGER MENU ITEMS
    ALL_ITEMS_MENU_ITEM = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    ABOUT_MENU_ITEM = (By.CSS_SELECTOR, "#about_sidebar_link")
    LOGOUT_MENU_ITEM = (By.CSS_SELECTOR, "#logout_sidebar_link")
    RESET_APP_STATE = (By.CSS_SELECTOR, "#reset_sidebar_link")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "#react-burger-cross-btn")

    # SECONDARY HEADER
    PRODUCTS_TITLE = (By.CSS_SELECTOR, ".title")
    PRODUCT_SORT_FILTER = (By.CSS_SELECTOR, ".product_sort_container")

    """ FOOTERS """
    FOOTER_SECTION = (By.CSS_SELECTOR, ".footer")
    TWITTER_IMAGE_LINK = (By.CSS_SELECTOR, "li[class$='twitter'] a[target='_blank']")
    FACEBOOK_IMAGE_LINK = (By.CSS_SELECTOR, "li[class$='facebook'] a[target='_blank']")
    LINKEDIN_IMAGE_LINK = (By.CSS_SELECTOR, "li[class$='linkedin'] a[target='_blank']")
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, ".footer_copy")
    FOOTER_ROBOT_IMAGE = (By.CLASS_NAME, "footer_robot")

    """ SELLING ITEMS """
    BUTTONS_ADD_X = (By.XPATH, '//button[text()="Add to cart"]')
    BUTTONS_REMOVE_X = (By.XPATH, '//button[text()="Remove"]')

    BTN_BACK_TO_PRODUCT = (By.CSS_SELECTOR, "button[name = 'back-to-products']")

    # FIRST ITEM
    BACKPACK_ITEM_NAME = (
        By.XPATH,
        '//*[@id="inventory_item_container"]',
    )
    BACKPACK_ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt$='Backpack']")
    BACKPACK_PRODUCT_DESCRIPTION = (
        By.XPATH,
        '//*[@id="inventory_item_container"]',
    )
    BACKPACK_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]')
    BACKPACK_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    BACKPACK_BACK_BUTTON = (By.XPATH, '//*[@id="back-to-products"]')

    # SECOND ITEM
    BIKE_LIGHT_ITEM_NAME = (
        By.CSS_SELECTOR,
        "a[id='item_0_title_link'] .inventory_item_name",
    )
    BIKE_LIGHT_ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt*='Light']")
    BIKE_LIGHT_PRODUCT_DESCRIPTION = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[2]",
    )
    BIKE_LIGHT_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[2]")
    BIKE_LIGHT_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BIKE_LIGHT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")

    # THIRD ITEM
    BOLT_TSHIRT_ITEM_NAME = (
        By.CSS_SELECTOR,
        "a[id='item_1_title_link'] div[class*='name']",
    )
    BOLT_TSHIRT_ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt$='T-Shirt']")
    BOLT_TSHIRT_PRODUCT_DESCRIPTION = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[3]",
    )
    BOLT_TSHIRT_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[3]")
    BOLT_TSHIRT_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    BOLT_TSHIRT_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    # FOURTH_ITEM
    FLEECE_JACKET_ITEM_NAME = (
        By.CSS_SELECTOR,
        "a[id='item_5_title_link'] div[class*='item']",
    )
    FLEECE_JACKET_ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt*='Fleece']")
    FLEECE_JACKET_PRODUCT_DESCRIPTION = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[4]",
    )
    FLEECE_JACKET_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[4]")
    FLEECE_JACKET_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    FLEECE_JACKET_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-fleece-jacket")

    # FIFTH_ITEM
    ONESIE_ITEM_NAME = (
        By.CSS_SELECTOR,
        "a[id='item_2_title_link'] div[class='inventory_item_name']",
    )
    ONESIE_ITEM_IMAGE = (By.CSS_SELECTOR, "img[alt*='Onesie']")
    ONESIE_PRODUCT_DESCRIPTION = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[5]",
    )
    ONESIE_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[5]")
    ONESIE_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    ONESIE_REMOVE_BUTTON = (By.ID, "remove-sauce-labs-onesie")

    # SIXTH_ITEM
    RED_SHIRT_ITEM_NAME = (
        By.CSS_SELECTOR,
        "a[id='item_3_title_link'] div[class='inventory_item_name']",
    )
    RED_SHIRT_ITEM_IMAGE = (
        By.CSS_SELECTOR,
        "img[alt='Test.allTheThings() T-Shirt (Red)']",
    )
    RED_SHIRT_PRODUCT_DESCRIPTION = (
        By.XPATH,
        "(//div[@class = 'inventory_item_desc'])[6]",
    )
    RED_SHIRT_PRICE = (By.XPATH, "(//div[@class = 'inventory_item_price'])[6]")
    RED_SHIRT_ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button[name='add-to-cart-test.allthethings()-t-shirt-(red)']",
    )
    RED_SHIRT_REMOVE_BUTTON = (
        By.CSS_SELECTOR,
        "button[name='remove-test.allthethings()-t-shirt-(red)']",
    )


class FilterOptions:
    NAME_A_Z = (By.CSS_SELECTOR, 'option[value="az"]')
    NAME_Z_A = (By.CSS_SELECTOR, 'option[value="za"]')
    PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, 'option[value="lohi"]')
    PRICE_HIGH_TO_LOW = (By.CSS_SELECTOR, 'option[value="hilo"]')


class CartPageLocators:
    # SECONDARY HEADER
    SECONDARY_HEADER = (By.CSS_SELECTOR, "#header_container > div.primary_header")
    SECONDARY_HEADER_TITLE = (By.CSS_SELECTOR, ".title")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "#continue-shopping")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    QTY_BOX = (By.CSS_SELECTOR, ".cart_quantity")
    NAME_BIKE_LIGHT_CART = (By.CSS_SELECTOR, "#item_0_title_link")
    NAME_BOLT_T_SHIRT_CART = (By.CSS_SELECTOR, "#item_1_title_link")
    NAME_ONESIE_CART = (By.CSS_SELECTOR, "#item_2_title_link")
    NAME_RED_T_SHIRT_CART = (By.CSS_SELECTOR, "#item_3_title_link")
    NAME_BACKPACK_CART = (By.CSS_SELECTOR, "#item_4_title_link")
    NAME_JACKET_CART = (By.CSS_SELECTOR, "#item_5_title_link")
    DESCRIPTION_ITEM_CART = (By.CSS_SELECTOR, ".inventory_item_desc")
    PRICE_ITEM_CART = (By.CSS_SELECTOR, ".item_pricebar")
    ITEMS_IN_CART = (By.CSS_SELECTOR, ".cart_item_label")


class FirstItemPageLocators:
    # https://www.saucedemo.com/inventory-item.html?id=4
    INVENTORY_DETAILS_IMG_FIRST_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_FIRST_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_FIRST_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_FIRST_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_FIRST_ITEM = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack",
    )
    REMOVE_BUTTON_FIRST_ITEM = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    BACK_TO_PRODUCTS_BUTTON_FIRST_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class SecondItemPageLocators:
    # https://www.saucedemo.com/inventory-item.html?id=0
    INVENTORY_DETAILS_IMG_SECOND_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_SECOND_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_SECOND_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_SECOND_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_SECOND_ITEM = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bike-light",
    )
    REMOVE_BUTTON_SECOND_ITEM = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
    BACK_TO_PRODUCTS_BUTTON_SECOND_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class ThirdItemPageLocators:
    # https: // www.saucedemo.com / inventory - item.html?id = 1
    INVENTORY_DETAILS_IMG_THIRD_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_THIRD_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_THIRD_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_THIRD_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_THIRD_ITEM = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bike-light",
    )
    REMOVE_BUTTON_THIRD_ITEM = (By.CSS_SELECTOR, "#remove-sauce-labs-bike-light")
    BACK_TO_PRODUCTS_BUTTON_THIRD_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class FourthItemPageLocators:
    # https://www.saucedemo.com/inventory-item.html?id=5
    INVENTORY_DETAILS_IMG_FOURTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_FOURTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_FOURTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_FOURTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_FOURTH_ITEM = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bike-light",
    )
    REMOVE_BUTTON_FOURTH_ITEM = (By.CSS_SELECTOR, "#remove-sauce-labs-fleece-jacket")
    BACK_TO_PRODUCTS_BUTTON_FOURTH_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class FifthItemPageLocators:
    # https://www.saucedemo.com/inventory-item.html?id=2
    INVENTORY_DETAILS_IMG_FIFTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_FIFTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_FIFTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_FIFTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_FIFTH_ITEM = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    REMOVE_BUTTON_FIFTH_ITEM = (By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    BACK_TO_PRODUCTS_BUTTON_FIFTH_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class SixthItemPageLocators:
    # https://www.saucedemo.com/inventory-item.html?id=3
    INVENTORY_DETAILS_IMG_SIXTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_img")
    DETAILS_NAME_SIXTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_DESCRIPTION_SIXTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_desc")
    PRICE_BUTTON_SIXTH_ITEM = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON_SIXTH_ITEM = (
        By.CSS_SELECTOR,
        ".btn_primary.btn_small.btn_inventory",
    )
    REMOVE_BUTTON_SIXTH_ITEM = (
        By.CSS_SELECTOR,
        ".btn_secondary.btn_small.btn_inventory",
    )
    BACK_TO_PRODUCTS_BUTTON_SIXTH_ITEM = (By.CSS_SELECTOR, "#back-to-products")


class CheckOutYourInformationPage:
    # https: // www.saucedemo.com / checkout - step - one.html
    CHECKOUT_YOUR_INFORMATION_TEXT = (By.CSS_SELECTOR, ".title")
    CHECKOUT_INFO_FORM = (By.CSS_SELECTOR, ".checkout_info")
    CHECKOUT_FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    CHECKOUT_LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, "#postal-code")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    PRIMARY_HEADER = (By.CSS_SELECTOR, "#header_container")
    ERROR_FIRST_NAME = (By.XPATH, "//h3[@data-test='error']")
    ERROR_LAST_NAME = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3",
    )
    ERROR_POSTAL_ZIPCODE = (
        By.XPATH,
        "/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3",
    )


class CheckOutOverviewPage:
    # https: // www.saucedemo.com / checkout - step - two.html
    HEADER_OVERVIEW = (By.CSS_SELECTOR, "#header_container")
    CHECKOUT_OVERVIEW_TEXT = (By.CSS_SELECTOR, ".title")
    QUANTITY_LABEL = (By.CSS_SELECTOR, ".cart_quantity_label")
    DESCRIPTION_LABEL = (By.CSS_SELECTOR, ".cart_desc_label")
    PAYMENT_INFORMATION_LABEL = (By.CSS_SELECTOR, ".summary_info div:nth-child(1)")
    SUMMARY_VALUE_LABEL = (By.CSS_SELECTOR, ".summary_info div:nth-child(2)")
    SHIPPING_INFORMATION = (By.CSS_SELECTOR, ".summary_info div:nth-child(3)")
    FREE_PONY_EXPRESS_DELIVERY_LABEL = (
        By.CSS_SELECTOR,
        ".summary_info div:nth-child(4)",
    )
    ITEM_TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX_LABEL = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "#cancel")
    FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")


class CheckOutCompletePage:
    # https://www.saucedemo.com/checkout-complete.html
    CHECKOUT_COMPLETE_LABEL = (By.CSS_SELECTOR, ".title")
    THANK_YOU_LABEL = (By.CSS_SELECTOR, "complete-header")
    YOUR_ORDER_DISPATCHED_LABEL = (By.CSS_SELECTOR, ".complete-text")
    BACK_HOME_BUTTON = (By.CSS_SELECTOR, "#back-to-products")
    HEADER_COMPLETE_PAGE = (By.CSS_SELECTOR, "#header_container")
