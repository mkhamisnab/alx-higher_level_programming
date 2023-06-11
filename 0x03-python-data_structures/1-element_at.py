#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the specified index in the list.
        Returns None if the index is out of range.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return my_list[idx]
