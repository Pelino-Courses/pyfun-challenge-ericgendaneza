def format_text(text:str, prefix:str ="", suffix:str="", capitalize: bool = False, max_length:int = None) -> str:
    """
    Format the input text by adding a prefix and suffix, capitalizing it, and limiting its length.

    Parameters:
    text (str): The input text to format.
    prefix (str, optional): The prefix to add to the text. Defaults to "".
    suffix (str, optional): The suffix to add to the text. Defaults to "".
    capitalize (bool, optional): Whether to capitalize the text. Defaults to False.
    max_length (int, optional): The maximum length of the formatted text. If exceeded, raises ValueError. Defaults to None.

    Returns:
    str: The formatted text.

    Raises:
    ValueError: If the formatted text exceeds max_length or if the input is invalid.

    Examples:
    $ format_text("hello world", prefix="$ ", suffix=" !", capitalize=True, max_length=20)
    '$ HELLO WORLD !'

    $ format_text("hello world", max_length=5)
    Traceback (most recent call last):
        ...
    ValueError: Formatted text exceeds maximum length of 5 characters.
    """

    # Validate inputs
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    if not isinstance(prefix, str) or not isinstance(suffix, str):
        raise ValueError("Prefix and suffix must be strings.")

    if not isinstance(capitalize, bool):
        raise ValueError("Capitalize must be a boolean value.")

    if max_length is not None and not isinstance(max_length, int):
        raise ValueError("max_length must be an integer or None.")

    # Apply transformations
    formatted_text = f"{prefix}{text}{suffix}"

    if capitalize:
        formatted_text = formatted_text.upper()

    if max_length is not None and len(formatted_text) > max_length:
        raise ValueError(f"Formatted text exceeds maximum length of {max_length} characters.")

    return formatted_text

# Example usage

try:
    formatted_text = format_text("hello world", prefix="$ ", suffix=" !", capitalize=True, max_length=20)
    print(formatted_text)  # Output: "$ HELLO WORLD !"

    formatted_text = format_text("hello world", max_length=5)
    print(formatted_text)  # Output: "ValueError"

except ValueError as e:
    print(e)
