#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list): The list containing the integers to be printed in reverse order.

    Returns:
        None

    Note:
        If the input is not a list, the function will not perform any action.
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
