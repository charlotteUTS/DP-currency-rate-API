import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """

    #initialize the object’s attributes 
    def __init__(self, from_currency, to_currency, date):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.amount = 1


    def check_currencies(self):

        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        self: CurrencyConverter

        Pseudo-code
        ----------
        Create function "check_currencies"
        Instantiate object from Frankfurter as ff_obj
        IF from currency code and to_currency code are invalid
            Exit and display the relevent message
        ELSE IF  to currency code is invalid
            Exit and display the relevent message if to_currency is invalid
        ELSE IF from currency code is invalid
            Exit and display the relevent message
        ELSE return True

        Returns
        -------
        Return SystemExit and display relevent message if the currency code is invalid
        Return True if both from_currency and to_currency code are valid
        """

        ff_obj = Frankfurter()
        if not Frankfurter.check_currency(ff_obj, self.from_currency) and not Frankfurter.check_currency(ff_obj, self.to_currency):
            sys.exit(self.from_currency + " and " + self.to_currency + " are not valid currency code")
        elif not Frankfurter.check_currency(ff_obj, self.to_currency):
            sys.exit(self.to_currency + " is not a valid currency code")
        elif not Frankfurter.check_currency(ff_obj, self.from_currency):
            sys.exit(self.from_currency + " is not a valid currency code")
        else:
            return True
    
   
    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        self: CurrencyConverter

        Pseudo-code
        ----------
        Create function "reverse_rate"
            round up the reverse rate to 4 decimal places
            return the inverse rate

        Returns
        -------
        Return the rounded up inverse rate
        """
        self.inverse_rate = round(1 / self.rate, 4)
        return self.inverse_rate



    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        self: CurrencyConverter
        rate: float

        Pseudo-code
        ----------
        Create function "round_rate"
            return the rate rounded up to 4 decimals places

        Returns
        -------
        Return the round rate in 4 decimals places
        """
        return round(rate, 4)


    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        self: CurrencyConverter

        Pseudo-code
        ----------
        Create function "get_historical_rate"
            Instantiate object from Frankfurter as ff_obj
            call function get_historical_rate from Frankfurter and save the response as resp
            Get resp in json format and save as rate
            Round up the rate to 4 decimal place by calling function round_rate and save as rate
            Get the inverse rate by calling function reverse rate and save as inverse_rate
            SystemExit and display the relevent message

        Returns
        -------
        Return SystemExit and display the message with conversion rate and inverse rate
        """
       
        ff_obj = Frankfurter()
        resp = Frankfurter.get_historical_rate(ff_obj, self.from_currency.upper(), self.to_currency.upper(), self.date)
        rate = resp.json()['rates'][self.to_currency.upper()]
        self.rate = CurrencyConverter.round_rate(self, rate)
        self.inverse_rate = CurrencyConverter.reverse_rate(self)
        sys.exit("The conversion rate on " + self.date + " from " + self.from_currency + " to " + self.to_currency + \
            " was " + "{:.4f}".format(self.rate) + ". The inverse rate was " + "{:.4f}".format(self.inverse_rate))

