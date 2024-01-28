import unittest
from checks import check_arguments, check_date



class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """

    # zero argument
    def test_zero_arg(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments([])
        self.assertTrue(cm.exception.code)

    # one argument

    def test_one_arg(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments(["2022-01-01"])
        self.assertTrue(cm.exception.code)

    # two argument

    def test_two_arg(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments(["2022-01-01", "AUD"])
        self.assertTrue(cm.exception.code)

    # Three argument

    def test_three_arg(self):
        self.assertEqual(len(check_arguments(["2022-01-01", "AUD", "EUR"])), 3)

    # Four argument

    def test_four_arg(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments(["2022-01-01", "AUD", "EUR", "GBP"])
        self.assertTrue(cm.exception.code)



class TestCheckDate(unittest.TestCase):

    """
    Class used for testing the check_date() function from checks.py
    """

    # Valid date

    def test_1(self):
        self.assertTrue(check_date("2000-01-01"))

    # Invalid Year

    def test_2(self):
        with self.assertRaises(SystemExit) as cm:
            check_date("1990-01-01")
            check_date("2030-01-01")
            check_date("20-01-01")            
            check_date("20222-01-01")
        self.assertTrue(cm.exception.code)

    # Invalid format

    def test_3(self):
        with self.assertRaises(SystemExit) as cm:
            check_date("2022/01/01")
            check_date("20220101")
            check_date("01/01/2022")            
        self.assertTrue(cm.exception.code)      

    # Invalid date

    def test_4(self):
        with self.assertRaises(SystemExit) as cm:
            check_date("2022-01-41")
            check_date("2022-01-00")
            check_date("2010-01-1")
        self.assertTrue(cm.exception.code)

    # Invalid Month

    def test_5(self):
        with self.assertRaises(SystemExit) as cm:
            check_date("2000-13-01")
            check_date("2000-00-01")
            check_date("2000-111-01")
            check_date("2000_001-01")
            check_date("2010-1-01")
        self.assertTrue(cm.exception.code)

if __name__ == '__main__':
    unittest.main()
