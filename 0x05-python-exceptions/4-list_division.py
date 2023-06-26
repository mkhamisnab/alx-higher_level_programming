#!/usr/bin/python3

def safe_print_division(a, b):
"""Divides a by b and safely handles exceptions.

Args:
    a (float or int): The numerator.
    b (float or int): The denominator.

Returns:
    float or None: The result of the division, or None if an exception occurs.
"""
try:
    result = a / b
except (TypeError, ZeroDivisionError):
    result = None
finally:
    print("Inside result: {}".format(result))
return result
