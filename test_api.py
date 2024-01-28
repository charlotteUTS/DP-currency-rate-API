import unittest
from api import call_get


"""
Class used for testing the call_get() function in api.py
"""

class TestAPI(unittest.TestCase):

    
    """
    Class used for testing the call_get() function in api.py
    """

    # Test the call_get function with latest url
    def test_latest(self):
        url_latest = "https://api.frankfurter.app/latest"
        self.assertEqual(call_get(url_latest).status_code, 200)


    # Test the call_get function with currency url
    def test_cur(self):
        url_cur = "https://api.frankfurter.app/currencies"
        self.assertEqual(call_get(url_cur).status_code, 200)


    # Test the call_get function with historical url
    def test_his(self):
        url_his = "https://api.frankfurter.app/2022-03-11..?amount=100&from=AUD&to=HKD"
        self.assertEqual(call_get(url_his).status_code, 200)


    # Test an invalid url
    def test_error(self):
        url_error = "https://api.frankfurter.app/1234"
        with self.assertRaises(SystemExit) as cm:
            call_get(url_error)
        self.assertTrue(cm.exception.code)
   

if __name__ == '__main__':
    unittest.main()


