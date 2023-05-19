import unittest

from requests_folder.simple_books_requests import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_update_order_status_code(self):
        book_id = 1
        customer_name = "Paula"

        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_order_response = 201
        actual_order_response = place_order_response.status_code

        self.assertEqual(expected_order_response, actual_order_response, "Unexpected status code for new order")

        order_id = place_order_response.json()["orderId"]
        new_customer_name = "PaulaIoanaOprea"
        update_order_response = self.books_api.update_order(self.access_token, order_id, new_customer_name)

        expected_update_status_code = 204
        actual_update_status_code = update_order_response.status_code

        self.assertEqual(expected_update_status_code, actual_update_status_code,
                         "Unexpected status code for update order")
