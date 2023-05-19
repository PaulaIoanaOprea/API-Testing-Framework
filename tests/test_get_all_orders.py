import unittest


from requests_folder.simple_books_requests import SimpleBooksRequests


class TestGetAllOrders(unittest.TestCase):

    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_get_all_orders_status_code(self):
        book_id = 1
        customer_name = "Paula"

        place_order_response = self.books_api.submit_order(self.access_token, book_id, customer_name)

        expected_order_response = 201
        actual_order_response = place_order_response.status_code

        self.assertEqual(expected_order_response, actual_order_response, "Unexpected status code for new order")

        response = self.books_api.get_all_orders(self.access_token)

        expected_status_code = 200
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Error, unexpected response code")

