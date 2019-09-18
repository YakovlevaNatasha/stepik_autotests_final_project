from .base_page import BasePage 
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def click_add_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

	def should_be_success_adding(self):
		isContainedMessage = self.is_element_present(*ProductPageLocators.GOOD_IS_ADDED_TO_BASKET_MSG)
		isCorrectNameOfGood = self.is_elements_same(*ProductPageLocators.NAME_OF_GOOD, *ProductPageLocators.NAME_FROM_MESSAGE)
		assert (isContainedMessage and isCorrectNameOfGood), "Message about success adding of good in basket is not contained at this page or name of good is wrong"
	

	def should_be_message_with_basket_price(self):
		isContainedMessage = self.is_element_present(*ProductPageLocators.MESSAGE_WITH_BASKET_PRICE)
		isPriceMatch = self.is_elements_same(*ProductPageLocators.BASKET_PRICE, *ProductPageLocators.PRICE)
		assert (isPriceMatch and isContainedMessage), "Price of basket and price of good are different!" 

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.GOOD_IS_ADDED_TO_BASKET_MSG), \
			"Success message is presented, but should not be"

	def should_not_is_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.GOOD_IS_ADDED_TO_BASKET_MSG), \
			"Success message is disappeared, but should not be"
