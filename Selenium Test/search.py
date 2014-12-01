import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SearchPage(unittest.TestCase):
	def __init__(self):
		return None

	def setUp(self):
		self.driver = webdriver.Firefox() 

	def search(self):
		driver = self.driver
		driver.get("https://tokopedia.com/")
		elem = driver.find_element_by_name("search_keyword")
		elem.send_keys("Nokia")
		assert "No result found." not in driver.page_source
		elem.send_keys(Keys.RETUNR)

	def tearDown(self):
		self.driver.close()

	def __str__(self):
		return "Class Search"

# main

if(__name__ == "__main__"):
	unittest.main()