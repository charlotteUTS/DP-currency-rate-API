import datetime
import sys


def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    args: string
    The input argument

    Pseudo-code
    ----------
    Create function "check_arguments"
        IF the length of argument is not equal to 3 
            System Exit and display error message stating missing argument
        ELSE
            RETURN argument list

    Returns
    -------
    Return input arguments 
    """
    if len(args) != 3:
        sys.exit("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
    else:
        return args


def check_date(date):

    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    date: Str
    the input date argument

    Pseudo-code
    ----------
    Create function "check_date"
        split the input date by '-'
        IF the length of year is not equal to 4 or the length of month is not equal to 2 or the length of dates is not equal to 2  
            System Exit and display the relevent message
        let today as today's date in format %Y-%m-%d
        try
            test if the input date is in the format %Y-%m-%d
        except the format of date is incorrect
            SystemExit and display the relevent message
        IF date is between "1999-01-04" and today
            RETURN True
        ELSE
            SystemExit and display the relevent message

    Returns
    -------
    Return SystemExit and display the relevent message if the date is invalid
    Return TRUE if the date is valid

    """
    # Check the format of date
    date_split = date.split('-')
    if len(date_split[0]) != 4 or len(date_split[1]) != 2 or len(date_split[2]) !=2 :
        sys.exit("Provided date is invalid")
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    try:
        datetime.datetime.today().strptime(date, '%Y-%m-%d')
    except ValueError:
        sys.exit("Provided date is invalid")

    if date >= "1999-01-04"  and date <= today:
        return True
    else:
        sys.exit("Provided date is invalid")

