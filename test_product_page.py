import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

 #@pytest.mark.parametrize('link',
     #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail(reason="падает")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.remember_product_name_and_price()
#
#     page.solve_quiz_and_get_code()
#     time.sleep(2)
#     page.check_product_name_and_price_after_add_to_card()
link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open() #Открываем страницу товара
    page.add_product_to_cart() # Добавляем товар в корзину
    page.should_not_be_success_message()  #Проверяем, что нет сообщения об успехе с помощью is_not_element_present



def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

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

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()