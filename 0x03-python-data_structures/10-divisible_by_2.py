#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        list: A new list with boolean values indicating whether each element is divisible by 2.

    Examples:
        divisible_by_2([1, 2, 3, 4]) returns [False, True, False, True]
        divisible_by_2([]) returns []
    """
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
