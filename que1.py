from datetime import datetime

def date_difference(date1:str, date2:str)-> int:
    """
    Calculate the difference between two dates in days.

    Parameters:
    date1 (str): The first date in 'YYYY-MM-DD' format.
    date2 (str): The second date in 'YYYY-MM-DD' format.

    Returns:
    int: The difference in days between the two dates.

    Raises:
    ValueError: If the date format is incorrect.

    example:
    >>> date_difference('2023-10-01', '2023-10-15')
    14
    >>> date_difference('2023-10-01', '2023-09-15')
    -16
    >>> date_difference('2023-10-01', '2023-10-01')
    0
    """
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return (d2 - d1).days
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")

# Example usage
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

try:
    difference = date_difference(date1, date2)
    print(f"The difference between {date1} and {date2} is {difference} days.")
except ValueError as e:
    print(e)
