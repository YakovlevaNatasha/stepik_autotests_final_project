#from .pages.main_page import MainPage 
from .pages.login_page import LoginPage 

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    #page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page = LoginPage(browser, link)
    page.open()  # открываем страницу
    page.should_be_login_url()  # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_form()
    page.should_be_register_form()