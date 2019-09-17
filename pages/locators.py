from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
	GOOD_IS_ADDED_TO_BASKET_MSG = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
	PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
	MESSAGE_WITH_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info p")
	BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info p strong")
	NAME_OF_GOOD = (By.CSS_SELECTOR, ".product_main h1")
	NAME_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")