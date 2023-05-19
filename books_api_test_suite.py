import unittest

import HtmlTestRunner

from requests_folder.simple_books_requests import SimpleBooksRequests
from tests.test_api_status import TestApiStatus
from tests.test_delete_order import TestDeleteOrder
from tests.test_get_a_single_book import TestGetSingleBook
from tests.test_get_all_books import TestGetAllBooks
from tests.test_get_all_orders import TestGetAllOrders
from tests.test_submit_order import TestSubmitOrder
from tests.test_update_order import TestUpdateOrder
from tests.test_get_a_single_order import TestGetSingleOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suita_teste = unittest.TestSuite()

        # adaugam testele in suita
        suita_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(SimpleBooksRequests),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetSingleBook),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllOrders),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetSingleOrder)

        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API test report",
            report_name="Books API Test Results"
        )

        runner.run(suita_teste)

