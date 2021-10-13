from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class InventoryProtocolDriver(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def _confirm_is_admin(self):
        self.assertEquals(self.browser.title, "Dave's Book Store - Admin")

    def add_book(self, title, author):
        self._confirm_is_admin()
        self.browser.find_element_by_name("bookTitle").send_keys(title)
        self.browser.find_element_by_name("bookAuthor").send_keys(author)
        self.browser.find_element_by_name("AddButton").click()
