from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def in_basket_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "has items, but should not be"

    def is_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "empty message is not shown"

