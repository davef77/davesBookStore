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

    def search_for_books(self):
        pass

    def confirm_books_found(self, param, param1):
        pass


