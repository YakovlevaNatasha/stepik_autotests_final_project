import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

@pytest.mark.need_review
@pytest.mark.parametrize('offerNumb', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offerNumb):
    product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + offerNumb
    page = ProductPage(browser, product_link) 
    page.open()  
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_adding()
    page.should_be_message_with_basket_price()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_goods_in_basket()
    basket_page.should_be_basket_is_empty_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_success_message(browser):      
    page = ProductPage(browser, link) 
    page.open()  
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#negative reverse test
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_not_be_success_message()

#negative reverse test
@pytest.mark.skip 
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_not_is_disappeared()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, '12df34gh56yu')
        page.should_be_authorized_user()   

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link) 
        page.open()  
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link) 
        page.open()  
        page.click_add_to_basket()
        page.should_be_success_adding()