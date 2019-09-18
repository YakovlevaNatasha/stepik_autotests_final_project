from .base_page import BasePage 
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_be_basket_is_empty_message(self):
		message = self.get_text_of_element(*BasketPageLocators.EMPTY_BASKET_MSG)
		if message.find("Ваша корзина пуста."):	
			assert True
		elif message.find("Votre panier est vide."):	
			assert True
		elif message.find("Your basket is empty."):	
			assert True
		elif message.find("Il tuo carrello è vuoto."):	
			assert True
		else:
			assert False, "The basket is not empty or you should select another language"

	def should_be_goods_in_basket(self):
		assert not self.is_not_element_present(*BasketPageLocators.CONTAINER_OF_GOODS), "Basket is empty, but shouldn't be"


	def should_not_be_goods_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.CONTAINER_OF_GOODS), "Basket is not empty, but should be"