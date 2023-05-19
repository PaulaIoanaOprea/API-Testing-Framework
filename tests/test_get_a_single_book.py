import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestGetSingleBook(unittest.TestCase):

    def setUp(self):
        self.books_api = SimpleBooksRequests()

    def test_get_a_single_book_status_code(self):
        response = self.books_api.get_a_single_book(book_id=2)

        expected_status_code = 200
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Error, unexpected response code")
