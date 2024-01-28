# AT1 - Building Currency Converter in Python

## Author
Name: Li Cheuk Wing Chering 

Student ID: 24586303

University of Technology Sydney - 94692 Data Science Practice


## Table of Contents

- [Program Description]
- [Challenges]
- [Potential additional feature]
- [How to Setup]
- [Packages]
- [How to Run the Program]
- [Invalid input argument]
- [Project Structure]
- [Citations]

## Program Description
This Python program convert currencies using data fetched from an open-source API "Frankfurter". This API provide the real-time exchange rate and historical rate. Two API endpoints from the Frankfurter app are used:

1. Extracting the currency list: https://www.frankfurter.app/currencies
![](/Users/charlotteli/Desktop/Screenshot 2022-09-07 at 6.24.57 PM.png)

2. Extracting the historical conversion rate for the specified currency codes and date:\
https://www.frankfurter.app/{from_date}?amount={amount}&from={from_currency}&to={to_currency}

e.g. https://api.frankfurter.app/2022-01-01?amount=1&from=AUD&to=HKD \
It will extract the conversion rate for AUD to HKD on 2022-01-01
![](/Users/charlotteli/Desktop/Screenshot 2022-09-07 at 6.03.05 PM.png){width=70%}

The user inputs three arguments (Date, To_currency and From_currency) and the system will return the conversion rate and the reverse rate between these 2 currencies at a specific date.

## Challenges
<Some of the challenges you faced>
<Some of the features you hope to implement in the future>

Building this converter is very challenging for me. I kept finding different bugs, it is difficult to identify the problem and fix it properly. For instance, I found that my program cannot read the input currency code in lower case and it will treat it as an invalid currency code. As a result, I spent some time fixing the problem by using the upper() function to turn the input currency code from low case to upper case.

## Potential additional feature

While this converter can only provide the exchange rate and reverse rate of two currencies at a specific date, there are potential functions that may advance the converter. I think the converter can show the difference in exchange rates within a period. The user inputs two dates, then the converter calculates the difference in rate between two days. For example, aud/hkd was 5.6569 on 2022-01-01, aud/hkd was 5.5375 on 2022-05-02, the program will output -0.1194.

## How to Setup

To set up the python environment before running the program, we need to install packages “requests”. The other module comes packaged with Python, so we don’t need to install it separately.
To install the requests library, type the following code in the terminal:

```python
# Check if the package Requests is already installed 
python -m pip show requests 
```
```python
# Install the package if not installed
pip install requests
```

Besides, please remember to check the connection with the internet which is need for connecting the Frankfurter API endpoint! \
My Python Version: 3.9.12 version \
Packages Version:\
Request: 2.28.1 \
DateTime: 4.5

### Packages

To support the program, the following packages are imported:

| Package | Usage | Example function |
| :--|:----|:----|
| 1. sys | Perform system exit when error occur | sys.exit() |
| 2. request | Used to extract response from  the API endpoint | response = requests.get(url)  |
| 3. unittest | Include methods for unittests | self.assertTrue(cm.exception.code) |
| 4. datetime | Provide functions to deal with dates  | datetime.datetime.today()  |

## How to Run the Program

To run the program, what we need to do is input 3 arguments(Date From_Currency To_Currency). The date should under the format YYY-MM-DD and the currency codes should be 3 digits. For example, if we want to know the conversion rate of AUD and HKD on 2022-01-01, our input should be **"python main.py 2022-01-01 AUD HKD"**. The system will return the conversion rate of AUD and HKD and their reverse rate which is the conversion rate of HKD and AUD like this: **The conversion rate on 2022-01-01 from AUD to HKD was 5.6569. The inverse rate was 0.1768**

```python
python main.py 2022-01-01 AUD HKD 
```

### Invalid input argument

When we input some invalid argument, the system will exit and display the relevant message to inform the user the mistake.\ Below are some of the example:

| Scenario | Input Example | Relevant message |
| :--|:---|:------|
| Missing argument | python main.py 2022-01-01 | [ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>|
| Invalid currency code | python main.py 2022-01-01 AUD HK | HK is not a valid currency code |
| Incorrect format of date | python main.py 2022/01/01 AUD HKD | Provided date is invalid |
| Invalid date | python main.py 2222-01-01 AUD HKD | Provided date is invalid |

## Project Structure

The program includes the following files:

| File | Usage | Function |
| :-|:--------|:---------|
| main.py | Main program for running the whole program logics | Call check_arguments, check_date(from check) ; check_currencies, get_historical_rate(from currency) |
| checks.py | Program for checking the input arguments and date validity  | check_date, check_arguments |
| api.py | Call the API endpoint and return its response | call_get |
| frankfurter.py | Mange the API for currencies list and historical rate ; Check the validity of currency code | init, get_currencies_list, check_currency, get_historical_rate |
| currency.py | Extracting currency conversion rate and calculating the round rate and inverse rate | init, check_currencies, reverse_rate,round_rate,get_historical_rate |
| test_checks.py | Testing code from checks.py with situation: 1 to 4 input arguments; Valid or Invalid date with incorrect format and invalid date | test_zero_arg... test_four_arg; test_1....test_5 |
| test_frankfurter.py | Testing code from frankfurter.py: <br> 1. testing the attributes of Frankfurter class <br> 2. test the check_currency method with valid and invalid currency code <br> 3. Test the get_historical_rate function with status_code| test_curr, test_curr1; test_his |
| test_api.py | Testing code from api.py with valid and invalid API | test_latest, test_cur, test_his, test_error |
| test_currency.py | Testing code from currency.py with valid and invalid currency code; check the method reverse_rate and round_rate in different situation | test_init, test_curr_check0, test_curr_check1...test_curr_check3, test....test3 |



## Citations
<Mention authors and provide links code you source externally>
Lathkar, M. (2021, January 5). Convert string to Datetime in python. Retrieved September 6, 2022, from https://www.tutorialsteacher.com/articles/convert-string-to-datetime-in-python 
