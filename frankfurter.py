from api import call_get


class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """

    def __init__(self):
        self.base_url = 'https://api.frankfurter.app/' 
        self.currencies_url = 'currencies'


    def get_currencies_list(self):  
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        Self: Frankfurter

        Pseudo-code
        ----------
        Create function "get_currencies_list"
        Create url as base_url + currencies_url
        call function call_get with url and save as resp
        get the list format of resp and save as currencies
        return currencies

        Returns
        -------
        Return the currency list extracted from Frankfurter API
        """   
        url = self.base_url + self.currencies_url
        resp = call_get(url)
        self.currencies = list(resp.json())
        return self.currencies


    # Check the validity of currency code
    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        self: Frankfurter
        currency: Str
        the input currency code

        Pseudo-code
        ----------
        Create function "check_currency"
        Extracting the currencies list by calling function get_currencies_list and save as code
        FOR each elements in the currencies list
            IF the input upper case currency code is equal to the element  in the currencies list
                RETURN True
        RETURN False

        Returns
        -------
        Return True if the code is in currencies list
        Return False if the code is not in currencies list
        """
        code = Frankfurter.get_currencies_list(self)
        for i in code:
            if currency.upper() == i:
                return True
        return False



    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        self: Frankfurter
        from_currency: Str
        the input from currency code
        to_currency: Str
        the input to currency code
        from_date: str
        the input date
        amount: int
        Convert amount with default value 1

        Pseudo-code
        ----------
        Create function "get_historical_rate"
        create variable historical_url
        create variable url as self.base_url + historical_ur
        call function call_get with input url and save the response object as historical_obj
        RETURN the response object

        Returns
        -------
        return the respose from frankfather endpoint with the historical rate
        """
        self.historical_url = f'{from_date}?amount={amount}&from={from_currency}&to={to_currency}'
        url = self.base_url + self.historical_url
        historical_obj = call_get(url)
        return historical_obj

