import unittest

from dsl.book_shopping_dsl import BookShoppingDSL
from dsl.inventory_dsl import InventoryDSL


class BookShoppingAcceptanceTestCase(unittest.TestCase):
    book_shopping: BookShoppingDSL
    inventory: InventoryDSL

    def setUp(self):
        self.book_shopping = BookShoppingDSL()
        self.inventory = InventoryDSL()


if __name__ == '__main__':
    unittest.main()
