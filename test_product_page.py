import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear"
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open() #Открываем страницу товара
    page.add_product_to_cart() # Добавляем товар в корзину
    page.should_not_be_success_message()  #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.registration_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page=LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()
        page.register_new_user(email=str(time.time()) + "@fakemail.org", password=str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  # Открываем страницу тов
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.remember_product_name_and_price()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        time.sleep(2)
        page.check_product_name_and_price_after_add_to_card()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_product_to_cart()  # Добавляем товар в корзину
    page.should_success_message_is_disappeared()  #Проверяем, что нет сообщения об успехе с помощью is_disappeared#

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.in_basket_no_items()
    basket_page.is_basket_empty_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.remember_product_name_and_price()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.check_product_name_and_price_after_add_to_card()
