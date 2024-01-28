import requests
import sys


def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    url: str
    url to Frankfurter API

    Pseudo-code
    ----------
    Create function call_get
        extract response from url endpoint and save as response
        IF the url is invalid (the status code of the response is not equal to 200)
            SystemExit and display the relevent message
        RETURN response 

    Returns
    -------
    Return response as a requests.models.Response object

    """
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit("There is an error with Frankfurter API")
    return response

 
