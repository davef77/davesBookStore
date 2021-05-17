from dsl.acceptance_test_case import BookShoppingAcceptanceTestCase


class EnterTheStoreTest(BookShoppingAcceptanceTestCase):

    def test_should_enter_the_store(self):
        self.book_shopping.visit_store()
        self.book_shopping.confirm_in_store()
