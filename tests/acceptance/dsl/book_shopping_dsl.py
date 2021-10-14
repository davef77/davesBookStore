from dsl import params
from dsl.web_store_pd import WebBookstoreProtocolDriver


class BookShoppingDSL:
    def __init__(self):
        self.driver = WebBookstoreProtocolDriver()
        self.driver.setUp()

    def visit_store(self):
        self.driver.visit_store()
        self.driver.confirm_in_store()

    def confirm_in_store(self):
        self.driver.confirm_in_store()

    def confirm_book_found(self, *args):
        self.visit_store()
        title = params.optional(args, 'title', "Continuous Delivery")
        self.driver.confirm_book_exists(title)
