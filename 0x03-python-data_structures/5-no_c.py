#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """
    Remove all occurrences of characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.

    Returns:
        str: A new string with all occurrences of 'c' and 'C' removed.

    Note:
        This function creates a new string without the characters 'c' and 'C'.
        The original string remains unchanged.
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
