#!/usr/bin/python3

import sys

def safe_function(fct, *args, **kwargs):
"""Executes a function safely.

Args:
    fct: The function to execute.
    args: Arguments for fct.
    kwargs: Keyword arguments for fct.

Returns:
    If an error occurs - None.
    Otherwise - the result of the call to fct.
"""
try:
    result = fct(*args, **kwargs)
    return result
except Exception as e:
    print("Exception: {}".format(e), file=sys.stderr)
    return None
