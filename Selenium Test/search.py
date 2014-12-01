from selenium import webdriver

class Search:
	def __init__(self):
		self.browser = webdriver.Firefox()
		self.browser.get("https://tokopedia.com/")
	
	def searchTkpd(self, sesuatu):
		self.browser.find_element_by_name("search_keyword").send_keys(sesuatu)
		self.browser.find_element_by_class_name("btn-search").click()
# main

if(__name__ == "__main__"):
	obj = Search()
	obj.searchTkpd("Toko QC 14")