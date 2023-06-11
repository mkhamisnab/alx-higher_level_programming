#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """
    Returns the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing two elements:
            - The length of the input string.
            - The first character of the input string.

    Note:
        If the input string is empty, the function returns a tuple with a length of 0
        and a value of None as the first character.

    Examples:
        multiple_returns("Hello") returns (5, 'H')
        multiple_returns("") returns (0, None)
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
