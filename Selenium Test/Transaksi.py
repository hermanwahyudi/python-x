from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import os

class Transaksi:
	
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

	def transactDeposit(self):
		self.browser.get("https://test.tokopedia.nginx/tokoqc14/produk-baru-terjamin")
		self.browser.find_element(By.ID, "btn-atc").click()
		randNotes = randint(1000000000000, 100000000000000)
		self.browser.find_element(By.ID, "notes").send_keys(randNotes)
		self.browser.find_element(By.CSS_SELECTOR, "button.btn-buy").click()
		self.browser.implicitly_wait(5)
		self.browser.find_element(By.ID, "input-gateway-0").click()
		self.browser.implicitly_wait(5)
		var = self.browser.find_element_by_id("btn-checkout").click()
		print(var)

# main

if(__name__ == "__main__"):
	obj = Transaksi()
	obj.transactDeposit()
