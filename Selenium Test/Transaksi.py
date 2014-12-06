from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import os

class Transaksi:
	
	# list domain toko
	domain_shop = ['tokoqc14', 'tokoqc15', 'tokoqc16']
	
	# dictionary
	dict = {
		"index_url" : "https://test.tokopedia.nginx/",
		"email" : "tkpd.qc+13@gmail.com",
		"password" : "1234asdf"
	}

	locators = {
		"atc" : "btn-atc"
	}

	def __init__(self):
		self.browser = webdriver.Chrome("chromedriver")
	
	def open(self, url):
		self.browser.get(url)

	def do_login(self):
		self.browser.find_element_by_link_text("Masuk").click()
		self.browser.find_element_by_name("email").send_keys(self.dict['email'])
		self.browser.find_element_by_name("pwd").send_keys(self.dict['password'])
		self.browser.find_element_by_class_name("btn-login-top").click()
		self.browser.implicitly_wait(5)

	def go_to_shop(self):
		length_shop = len(self.domain_shop)
		rand = randint(0, length_shop-1)
		self.open(self.dict['index_url'] + self.domain_shop[rand])

	def choose_product(self):
		self.go_to_shop()
		condition_product = self.browser.find_element(By.XPATH, "//div[@class='span9']/div[1]")
		if condition_product.text != "Tidak ada Produk":
			list_product = self.browser.find_elements(By.XPATH, "//div[@itemtype='http://schema.org/ItemList']/div")
			i, length = 0, len(list_product)
			rand = randint(i, length-1)
			print(length)
			while i < length:
				if(i == rand):
					list_product[i].click()
					break
				i += 1
			self.add_to_cart()
		else:
			print("Tidak ada Produk di Toko", self.browser.title)
	
	def add_to_cart(self):
		self.browser.implicitly_wait(5)
		var = self.browser.find_element(By.ID, "btn-atc").click()
		randNotes = randint(1000000000000, 100000000000000)
		self.browser.find_element(By.ID, "notes").send_keys(randNotes)

	def transact_deposit(self):
		return None
		
		#
		#randNotes = randint(1000000000000, 100000000000000)
		#self.browser.find_element(By.ID, "notes").send_keys(randNotes)
		#self.browser.find_element(By.CSS_SELECTOR, "button.btn-buy").click()
		#self.browser.implicitly_wait(5)
		#self.browser.find_element(By.ID, "input-gateway-0").click()
		#self.browser.implicitly_wait(5)
		#var = self.browser.find_element_by_id("btn-checkout").click()
		#print(var)

# main

if(__name__ == "__main__"):
	obj = Transaksi()
	obj.open(obj.dict['index_url'])
	obj.do_login()
	obj.choose_product()
	