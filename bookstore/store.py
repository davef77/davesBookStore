class Store:
    def __init__(self, book_list):
        self.books = book_list

    def list_books(self):
        return self.books.list()
