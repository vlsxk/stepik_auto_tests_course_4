from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_price_in_page = None
        self.product_name_in_page = None

    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
    def remember_product_name_and_price(self):
        self.product_name_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    def check_product_name_and_price_after_add_to_card(self):
        product_name_in_notify = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFY).text
        product_price_in_notify = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_NOTIFY).text
        assert self.product_name_in_page == product_name_in_notify, f"\nНазвание не совпадает: {self.product_name_in_page} != {product_name_in_notify}"
        assert self.product_price_in_page == product_price_in_notify, f"\nНазвание не совпадает: {self.product_price_in_page} != {product_price_in_notify}"



