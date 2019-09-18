from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login'), 'Uncorrect url! "Login" not contained in link'
     
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not contained at this page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not contained at this page"

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.get_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.get_element(*LoginPageLocators.PASSWORD_FIELD_REPEAT).send_keys(password)
        self.get_element(*LoginPageLocators.REGISTRATION_BUTTON).click()