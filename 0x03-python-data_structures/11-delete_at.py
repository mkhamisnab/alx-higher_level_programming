#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """
    Delete an item at a specific position in a list.

    Args:
        my_list (list): The input list.
        idx (int): The index of the item to delete.

    Returns:
        list: The modified list after deleting the item.

    Examples:
        delete_at([1, 2, 3, 4], 2) returns [1, 2, 4]
        delete_at([1, 2, 3, 4], 5) returns [1, 2, 3, 4]
        delete_at([], 0) returns []
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
