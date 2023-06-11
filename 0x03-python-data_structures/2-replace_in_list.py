#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.

    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index of the element to replace.
        element: The new element to be placed at the specified index.

    Returns:
        The modified list with the element replaced.
        If the index is out of range, the original list is returned unchanged.
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
