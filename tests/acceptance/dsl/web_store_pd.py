from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

BOOK_STORE_URL_ = 'http://bookstore:5000/'


class WebBookstoreProtocolDriver(TestCase):
    def setUp(self):
        # self.browser = webdriver.Chrome('./dsl/chromedriver')
        self.browser = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def confirm_in_store(self):
        self.assertEquals(self.browser.title, "Dave's Book Store")

    def visit_store(self):
        self.browser.get(BOOK_STORE_URL_)
