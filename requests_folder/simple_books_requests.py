import random
import unittest

import requests


class SimpleBooksRequests(unittest.TestCase):
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _ORDERS_ENDPOINT = "/orders"

    def generate_token(self):
        random_number = random.randint(1, 99999999999999999999999999999999999999999999)

        request_body = {
            "clientName": "name91",
            "clientEmail": f"random_mail{random_number}@example.com"
        }

        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT

        response = requests.post(auth_url, json=request_body)

        return response.json()["accessToken"]

    def get_api_status(self):

        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        result = requests.get(api_status_url)
        return result

    def get_all_books(self, book_type="", limit=""):

        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT

        if book_type != "" and limit == "":
            get_all_books_url = get_all_books_url + f"?type={book_type}"

        elif book_type == "" and limit != "":
            get_all_books_url = get_all_books_url + f"?limit={limit}"

        elif book_type != "" and limit != "":
            get_all_books_url = get_all_books_url + f"?type={book_type}&limit={limit}"

        result = requests.get(get_all_books_url)
        return result

    def get_a_single_book(self, book_id):

        get_a_single_book_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT + f"/{book_id}"

        result = requests.get(get_a_single_book_url)
        return result

    def submit_order(self, access_token, book_id, customer_name):

        submit_order_url = self._BASE_URL + self._ORDERS_ENDPOINT

        header_params = {"Authorization": access_token}

        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }
        result = requests.post(submit_order_url, json=request_body, headers=header_params)
        return result

    def get_all_orders(self, access_token):

        get_all_orders_url = self._BASE_URL + self._ORDERS_ENDPOINT

        header_params = {"Authorization": access_token}

        result = requests.get(get_all_orders_url, headers=header_params)
        return result

    def get_a_single_order(self, access_token, order_id):

        single_order_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        result = requests.get(single_order_url, headers=header_params)
        return result

    def update_order(self, access_token, order_id, new_customer_name):

        order_update_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        request_body = {
            "customerName": new_customer_name
        }

        result = requests.patch(order_update_url, json=request_body, headers=header_params)
        return result

    def delete_order(self, access_token, order_id):

        order_update_url = self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        result = requests.delete(order_update_url, headers=header_params)
        return result
