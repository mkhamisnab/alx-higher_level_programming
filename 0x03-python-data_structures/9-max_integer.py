#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """
    Find the biggest integer of a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The largest integer in the list.

    Note:
        If the input list is empty, the function returns None.

    Examples:
        max_integer([1, 2, 3, 4]) returns 4
        max_integer([]) returns None
    """
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return big
