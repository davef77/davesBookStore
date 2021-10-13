class Store:
    def __init__(self, book_list):
        self.books = book_list

    def list_books(self):
        books = []
        records = self.books.list_books()
        for record in records:
            books.append({'id': record[0], 'title': record[1], 'author': record[2]})
        return books

    def add_book(self, title, author):
        self.books.add([(title, author)])
