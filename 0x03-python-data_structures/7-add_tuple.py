#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    Args:
        tuple_a (tuple, optional): The first input tuple. Defaults to ().
        tuple_b (tuple, optional): The second input tuple. Defaults to ().

    Returns:
        tuple: A tuple containing the element-wise sum of the input tuples.

    Note:
        If a tuple has less than 2 elements, it is considered incomplete, and the
        missing elements are assumed to be 0. The function adds the corresponding
        elements of the input tuples and returns a new tuple with the sum.

    Examples:
        add_tuple((1, 2), (3, 4)) returns (4, 6)
        add_tuple((1,), (3,)) returns (4, 0)
        add_tuple((1, 2), ()) returns (1, 2)
        add_tuple((), ()) returns (0, 0)
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
