from dsl import params
from dsl.inventory_pd import InventoryProtocolDriver


class InventoryDSL:
    def __init__(self):
        self.driver = InventoryProtocolDriver()
        self.driver.setUp()

    def add_book(self, *args):
        title = params.optional(args, 'title', "Continuous Delivery")
        author = params.optional(args, 'author', "Dave")

        self.driver.add_book(title, author)

