from dsl.acceptance_test_case import BookShoppingAcceptanceTestCase


class SeeBooksForSaleAcceptanceTest(BookShoppingAcceptanceTestCase):

    def test_should_see_books_for_sale(self):
        self.inventory.add_book("book: A", "book: B")

        self.book_shopping.visit_store()
        self.book_shopping.search_for_books()
        self.book_shopping.confirm_books_found("book: A", "book: B")



