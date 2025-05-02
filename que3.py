def calculate(*args, **kwargs):
    """
    Perform calculations based on the provided positional and keyword arguments.

    Positional arguments are treated as numbers to be calculated.
    Keyword arguments represent operations to apply (e.g., add=True, multiply=True).

    Parameters:
    *args: Numbers to be calculated.
    **kwargs: Operations to apply (e.g., add=True, subtract=True).

    Returns:
    1. float: As the result of the calculation.
    2. dict: If multiple operations are specified, returns a dictionary with operation names as keys and results as values.

    Raises:
    ValueError: If an invalid operation is specified or if no numbers are provided.
    TypeError: If non-numeric values are provided in positional arguments.
    ZeroDivisionError: If division by zero is attempted.

    Example:
    1. calculate(1, 2, 3, add=True, multiply=True)
    6.0
    2. calculate(10, 5, subtract=True)
    5.0
    3. calculate(10, 0, divide=True)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero is not allowed.
    """
    if not args:
        raise ValueError("At least one number must be provided for calculation.")

    res_add = res_mult = res_sub = res_div = float(args[0])

    for num in args[1:]:
        if not isinstance(num, (int, float)):
            raise TypeError(f"Invalid input: {num}. Only numbers are allowed.")

        if 'add' in kwargs:
            res_add += num

        if 'subtract' in kwargs:
            res_sub -= num
        if 'multiply' in kwargs:
            res_mult *= num
        if 'divide' in kwargs:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            res_div /= num
    # checking length of kwargs to see which operation to return
    if len(kwargs) == 1:
        if 'add' in kwargs:
            return res_add
        elif 'subtract' in kwargs:
            return res_sub
        elif 'multiply' in kwargs:
            return res_mult
        elif 'divide' in kwargs:
            return res_div
    else:
        # if more than one operation is specified, return a tuple of results
        results = {}
        if 'add' in kwargs:
            results['add'] = res_add
        if 'subtract' in kwargs:
            results['subtract'] = res_sub
        if 'multiply' in kwargs:
            results['multiply'] = res_mult
        if 'divide' in kwargs:
            results['divide'] = res_div
        return results



# Example usage of the calculate function
try:
    print(calculate(1, 2, 3, add=True, multiply=True))
    print(calculate(10, 5, subtract=True))
    print(calculate(10, 0, divide=True))  # This will raise an exception

except (ValueError, TypeError, ZeroDivisionError) as e:
    print(f"Error: {e}")