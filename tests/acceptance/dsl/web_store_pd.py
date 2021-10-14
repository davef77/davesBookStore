import os
from unittest import TestCase

from dsl import acc_test_drivers


class WebBookstoreProtocolDriver(TestCase):
    def setUp(self):
        self.browser = acc_test_drivers.get_webdriver()
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def confirm_in_store(self):
        self.assertEqual(self.browser.title, "Dave's Book Store")

    def visit_store(self):
        url = "http://" + os.environ.get('BOOKSTORE_HOST') + ":" + os.environ.get('BOOKSTORE_PORT')
        self.browser.get(url)

    def confirm_book_exists(self, title):
        elements = self.browser.find_element_by_xpath("//div[@class='book']/div[text()='"
                                                      + title + "']")
        self.assertEqual(elements.text, title)





