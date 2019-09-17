from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
import time

class BasePage():
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")

	def get_element(self, how, what):
		return self.browser.find_element(how, what)

	def get_text_of_element(self, how, what):
		return self.get_element(how, what).text

	def is_elements_same(self, how_el1, what_el1, how_el2, what_el2):
		firstElement = self.get_text_of_element(how_el1, what_el1)
		secondElement = self.get_text_of_element(how_el2, what_el2)
		return (True if (firstElement == secondElement) else False)
