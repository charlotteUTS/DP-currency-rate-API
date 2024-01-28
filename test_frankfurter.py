import unittest
from frankfurter import Frankfurter

     
class TestUrl(unittest.TestCase):
    """""
    Class used for testing the url attributes of the Frankfurter class from Frankfurter.py
    """
    def test_url(self):
        test_obj = Frankfurter()
        self.assertEqual(test_obj.base_url, 'https://api.frankfurter.app/')
        self.assertEqual(test_obj.currencies_url, 'currencies')
        

class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from Frankfurter.py
    """
    def test_curr_list(self):
        test_obj = Frankfurter()
        result = Frankfurter.get_currencies_list(test_obj)
        self.assertIsInstance(result, list)

class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    # Test with Valid currency code "AUD", "HKD"
    def test_curr(self):
        test_obj = Frankfurter()
        self.assertTrue(Frankfurter.check_currency(test_obj, 'AUD'))
        self.assertTrue(Frankfurter.check_currency(test_obj, 'HKD'))
    

    # Test with invalid currency code "US", "USDD", "ABC"
    def test_curr1(self):
        test_obj = Frankfurter()
        self.assertFalse(Frankfurter.check_currency(test_obj, 'US'))
        self.assertFalse(Frankfurter.check_currency(test_obj, 'USDD'))
        self.assertFalse(Frankfurter.check_currency(test_obj, 'ABC'))


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    # Test the get_historical_rate function
    def test_his(self):
        obj = Frankfurter()
        his_obj = Frankfurter.get_historical_rate(obj, "AUD", "HKD", "2000-01-01")
        self.assertEqual(his_obj.status_code, 200)

if __name__ == '__main__':
    unittest.main()