import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    # test the constructor
    def test_init(self):
        test_obj = CurrencyConverter('AUD', 'HKD', '1999-01-04')
        self.assertEqual(test_obj.from_currency, 'AUD')
        self.assertEqual(test_obj.to_currency, 'HKD')
        self.assertEqual(test_obj.date, '1999-01-04')

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
    # Vaild argument
    def test_curr_check0(self):
        test_obj1 = CurrencyConverter('AUD','HKD','1999-01-04')
        test_obj2 = CurrencyConverter('aud','hkd','1999-01-04')
        test_obj3 = CurrencyConverter('Aud','HKd','1999-01-04')
        self.assertTrue(CurrencyConverter.check_currencies(test_obj1))
        self.assertTrue(CurrencyConverter.check_currencies(test_obj2))
        self.assertTrue(CurrencyConverter.check_currencies(test_obj3))


    # Invaild from_currency
    def test_curr_check1(self):
        test_obj = CurrencyConverter('AU','HKD','1999-01-04')
        with self.assertRaises(SystemExit) as cm:
            CurrencyConverter.check_currencies(test_obj)
        self.assertTrue(cm.exception.code)

    # Invaild to_currency
    def test_curr_check2(self):
        test_obj = CurrencyConverter('AUD','HK','1999-01-04')
        with self.assertRaises(SystemExit) as cm:
            CurrencyConverter.check_currencies(test_obj)
        self.assertTrue(cm.exception.code)

    # Invaild from_currency and to_currency
    def test_curr_check3(self):
        test_obj = CurrencyConverter('AU','HK','1999-01-04')
        with self.assertRaises(SystemExit) as cm:
            CurrencyConverter.check_currencies(test_obj)
        self.assertTrue(cm.exception.code)

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """

    # Check the reverse rate of 1.8649, correct result should be 0.5362.
    def test(self):
        test_obj = CurrencyConverter('','','')
        test_obj.rate = 1.8649
        self.assertEqual(CurrencyConverter.reverse_rate(test_obj), 0.5362)
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    # testing with more than 4 decimals
    def test1(self):
        test_obj = CurrencyConverter('','','')
        self.assertEqual(CurrencyConverter.round_rate(test_obj, 1.23456), 1.2346)
        self.assertEqual(CurrencyConverter.round_rate(test_obj, 1.23454), 1.2345)
        self.assertEqual(CurrencyConverter.round_rate(test_obj, 1.23499), 1.2350)

    # testing with less than 4 decimals
    def test2(self):
        test_obj = CurrencyConverter('','','')
        self.assertEqual(CurrencyConverter.round_rate(test_obj, 1.23), 1.2300)           


class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    def test3(self):
        test_obj = CurrencyConverter('GBP','AUD','2021-07-16')
        with self.assertRaises(SystemExit) as cm:
            CurrencyConverter.get_historical_rate(test_obj)
        self.assertTrue(cm.exception.code)
    
    
if __name__ == '__main__':
    unittest.main()