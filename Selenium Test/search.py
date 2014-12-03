from selenium import webdriver

class Search:
	def __init__(self):
<<<<<<< HEAD
		self.browser = webdriver.Firefox()
		self.browser.get("https://tokopedia.com/")
	
	def searchTkpd(self, sesuatu):
		self.browser.find_element_by_name("search_keyword").send_keys(sesuatu)
		self.browser.find_element_by_css_selector("button.btn-search").click()
		self.browser.find_element_by_id("tab-shop").click()
=======
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
>>>>>>> b_herman


# main

if(__name__ == "__main__"):
	obj = Search()
	obj.searchTkpd("Toko QC 14")
