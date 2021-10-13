import os
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebBookstoreProtocolDriver(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def confirm_in_store(self):
        self.assertEquals(self.browser.title, "Dave's Book Store")

    def visit_store(self):
        url = "http://" + os.environ.get('BOOKSTORE_HOST') + ":" + os.environ.get('BOOKSTORE_PORT')
        self.browser.get(url)




