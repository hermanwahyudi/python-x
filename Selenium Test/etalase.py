from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By

class Etalase:
	def __init__(self):
		#self.browser = webdriver.Firefox()
		self.browser = webdriver.Chrome('chromedriver')
		self.browser.get("https://test.tokopedia.nginx/myshop-etalase.pl")
		self.doLogin()
	
	def doLogin(self):
		self.browser.find_element_by_name("email").send_keys("tkpd.qc+13@gmail.com")
		self.browser.find_element_by_name("pwd").send_keys("1234asdf")
		self.browser.find_element_by_class_name("btn-login-top").click()


	def addEtalase(self):
		i = 0
		while i < 100:
			rand = randint(10000000, 99999999)
			self.browser.implicitly_wait(1)
			self.browser.find_element_by_id("btn-add").click()
			self.browser.find_element_by_name("e_name").send_keys(rand)
			self.browser.find_element_by_css_selector("button.btn-action").click()
			self.browser.get("https://test.tokopedia.nginx/myshop-etalase.pl")
			i += 1 

	def deleteEtalase(self):
		for i in range(10):
			self.browser.find_element_by_css_selector("a.delete-etalase").click()
			self.browser.implicitly_wait(6)
			self.browser.find_element_by_xpath("//button[@name='submit']").click()
			self.browser.get("https://test.tokopedia.nginx/myshop-etalase.pl")

# main

if(__name__ == "__main__"):
	 obj = Etalase()
	 obj.addEtalase()
	 obj.deleteEtalase()