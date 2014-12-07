from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
import os

class MyshopAddress:
	
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

	def inputAddress(self):
		i = 0
		while i < 1000:
			self.browser.get("https://test.tokopedia.nginx/people/1601633/address")
			rand01 = randint(10000000, 99999999)
			rand02 = randint(10000000000, 100000000000)
			#self.browser.implicitly_wait(5)
			self.browser.find_element(By.CSS_SELECTOR, 'a.actionlink-newadd-tab').click()
			self.browser.find_element(By.ID, 'addr_name').send_keys("243243243243243243243243243243243243")
			self.browser.find_element(By.ID, 'receiver_name').send_keys(rand01 + rand02)
			self.browser.find_element(By.ID, 'alamat').send_keys(rand01*2)
			self.browser.find_element(By.ID, 'postal_code').send_keys(rand01*2)
			op1 = self.browser.find_element(By.ID, 'provinsi')
			op1.find_element_by_xpath("//select/option[@value='17']").click()
			self.browser.implicitly_wait(5)
			op2 = self.browser.find_element(By.ID, 'kota')
			op2.find_element(By.XPATH, "//select/option[@value='259']").click()
			self.browser.implicitly_wait(19)
			op3 = self.browser.find_element(By.ID, 'kec')
			print(i)
			op3.find_element(By.XPATH, "//select/option[@value='3628']").click()
			# self.browser.find_element(By.XPATH, '//button[text()="Diskusi"]').click()
			self.browser.find_element(By.ID, 'kontak').send_keys(rand01)
			self.browser.find_element_by_xpath("//button[@name='submit']").click()
			i += 1 
	def uploadImage(self):
		self.browser.get("https://test.tokopedia.nginx/product-add.pl")
		self.browser.find_element_by_id("pickfiles").send_keys(os.getcwd()+"Desert.jpg")
		self.browser.find_element(By.XPATH, "//button[@id='s-save-prod']").click()

if(__name__ == "__main__"):
	obj = MyshopAddress()
	obj.uploadImage()
	#obj.inputAddress()
	#obj.deleteEtalase()
	#print(os.getcwd())