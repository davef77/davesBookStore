import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

BOOK_STORE_URL_ = 'http://localhost:5000/'


class WebBookstoreProtocolDriver(TestCase):
    def setUp(self):
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        # options = Options()
        # options.headless = True
        # # self.bookstore_url = self.live_server_url
        # self.browser = webdriver.Chrome(chrome_options=options)
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def confirm_in_store(self):
        self.assertEquals(self.browser.title, "Dave's Book Store")

    def visit_store(self):
        print("bookstore address:" + os.environ.get('BOOKSTORE_HOST') + ":" + os.environ.get('BOOKSTORE_PORT'))
        self.browser.get(os.environ.get('BOOKSTORE_HOST') + ":" + os.environ.get('BOOKSTORE_PORT'))
        # self.browser.get(self.bookstore_url)
