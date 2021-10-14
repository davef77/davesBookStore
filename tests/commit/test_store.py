import os
import unittest
from unittest.mock import Mock

from bookstore.store import Store


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.books = Mock()
        self.store = Store(self.books)

    def test_should_provide_list_of_books(self):
        self.books.list_books.return_value = [(1, 'title1', 'author1'),
                                              (2, 'title2', 'author2')]

        self.assertEqual([{'id': 1, 'title': 'title1', 'author': 'author1'},
                          {'id': 2, 'title': 'title2', 'author': 'author2'}],
                         self.store.list_books())

    def test_should_add_book_to_list(self):
        self.store.add_book('title1', 'author1')

        self.books.add.assert_called_with([('title1', 'author1')])