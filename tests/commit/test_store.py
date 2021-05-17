import unittest
from unittest.mock import Mock

from bookstore.store import Store


class StoreTest(unittest.TestCase):
    def test_should_provide_list_of_books(self):
        books = Mock()
        books.list.return_value = {'title': 'title1', 'author': 'author1'}
        store = Store(books)

        self.assertEqual({'title': 'title1', 'author': 'author1'}, store.list_books())


if __name__ == '__main__':
    unittest.main()
