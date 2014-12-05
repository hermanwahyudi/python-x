from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import os

class Product:
	
	#Dictionary
	dict1 = {}

	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get("https://test.tokopedia.nginx/")
		self.doLogin()
	
	def doLogin(self):
		self.browser.find_element_by_link_text("Masuk").click()
		self.browser.find_element_by_name("email").send_keys("tkpd.qc+13@gmail.com")
		self.browser.find_element_by_name("pwd").send_keys("1234asdf")
		self.browser.find_element_by_class_name("btn-login-top").click()
		self.browser.implicitly_wait(5)

	def addProduct(self):
		i = 1
		while i <= 100:
			self.browser.get("https://test.tokopedia.nginx/product-add.pl")
			randNameProd = randint(1000000000000, 10000000000000)
			randPrice = randint(100, 100000)
			randWeight = randint(100, 999)
			self.browser.find_element_by_id("p-name").send_keys(randNameProd)
			self.browser.find_element_by_id("p-price").send_keys(randPrice)
			self.browser.find_element_by_id("p-weight").send_keys(randWeight)
			self.browser.find_element_by_id("pickfiles").send_keys(os.getcwd()+"Desert.jpg")
			self.browser.find_element(By.XPATH, "//button[@id='s-save-prod']").click()
			print("Product bot ke-" + str(i))
			i += 1
# main

if(__name__ == "__main__"):
	obj = Product()
	obj.addProduct()
