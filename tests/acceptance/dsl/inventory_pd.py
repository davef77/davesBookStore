import os
from unittest import TestCase

from dsl import acc_test_drivers


class InventoryProtocolDriver(TestCase):
    def setUp(self):
        self.browser = acc_test_drivers.get_webdriver()
        self.addCleanup(self.browser.quit)

    def tear_down(self):
        self.browser.quit()

    def _confirm_is_admin(self):
        url = "http://" + os.environ.get('BOOKSTORE_HOST') + \
              ":" + os.environ.get('BOOKSTORE_PORT') + "/admin"
        self.browser.get(url)
        self.assertEqual(self.browser.title, "Dave's Book Store - Admin")

    def add_book(self, title, author):
        self._confirm_is_admin()
        self.browser.find_element_by_name("bookTitle").send_keys(title)
        self.browser.find_element_by_name("bookAuthor").send_keys(author)
        self.browser.find_element_by_name("AddButton").click()
