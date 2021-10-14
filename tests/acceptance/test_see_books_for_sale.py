from dsl.acceptance_test_case import BookShoppingAcceptanceTestCase


class SeeBooksForSaleAcceptanceTest(BookShoppingAcceptanceTestCase):

    def test_should_see_books_for_sale(self):
        self.inventory.add_book("title: A", "author: A1")
        self.inventory.add_book("title: B", "author: B1")

        self.book_shopping.visit_store()
        self.book_shopping.confirm_book_found("title: A")
        self.book_shopping.confirm_book_found("title: B")
