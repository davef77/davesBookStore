import unittest

from dsl.book_shopping_dsl import BookShoppingDSL


class BookShoppingAcceptanceTestCase(unittest.TestCase):
    book_shopping: BookShoppingDSL

    def setUp(self):
        self.book_shopping = BookShoppingDSL()


if __name__ == '__main__':
    unittest.main()
