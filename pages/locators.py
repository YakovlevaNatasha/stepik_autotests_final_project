from selenium.webdriver.common.by import By

class BasketPageLocators():
	#EMPTY_BUTTON_MSG = (By.XPATH, "//p[contains(text(),")
	EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")
	CONTAINER_OF_GOODS = (By.CSS_SELECTOR, ".basket_items")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn.btn-default:nth-child(1)')
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	PASSWORD_FIELD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
	ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
	GOOD_IS_ADDED_TO_BASKET_MSG = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
	PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
	MESSAGE_WITH_BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info p")
	BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info p strong")
	NAME_OF_GOOD = (By.CSS_SELECTOR, ".product_main h1")
	NAME_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
	BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn.btn-default:nth-child(1)')