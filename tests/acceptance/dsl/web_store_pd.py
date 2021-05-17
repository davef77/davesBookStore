from unittest import TestCase

from selenium import webdriver

BOOK_STORE_URL_ = 'http://localhost:5000/'


class WebBookstoreProtocolDriver(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./dsl/chromedriver')

    def tear_down(self):
        self.browser.quit()

    def confirm_in_store(self):
        self.assertEquals(self.browser.title, "Dave's Book Store")

    def visit_store(self):
        self.browser.get(BOOK_STORE_URL_)
