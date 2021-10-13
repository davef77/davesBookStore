import unittest
from unittest.mock import Mock

import booklist
from bookstore.store import Store
from dsl.inventory_dsl import InventoryDSL


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.books = Mock()
        self.store = Store(self.books)

    def test_should_provide_list_of_books(self):
        self.books.list_books.return_value = [(1, 'title1', 'author1'),
                                              (2, 'title2', 'author2')]

        self.assertEqual([{'id': 1, 'title': 'title1', 'author': 'author1'},
                          {'id': 2, 'title': 'title2', 'author': 'author2'}], self.store.list_books())

    def test_should_add_book_to_list(self):
        self.store.add_book('title1', 'author1')

        self.books.add.assert_called_with([('title1', 'author1')])

    def test_delme2(self):
        books = booklist
        y = books.add([('A', 'author1'),
                   ('B', 'author2')])

        for x in y:
            print(str(x[0]) + " " + x[1] + " " + x[2])


    def test_delme(self):
        books = booklist

        for x in books.list_books():
            print(str(x[0]) + " " + x[1] + " " + x[2])


    def test_inventory_DSL(self):
        dsl = InventoryDSL()

        dsl.add_book("author: Dave", "title: MSE")

if __name__ == '__main__':
    unittest.main()



