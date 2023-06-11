#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """
    Replace an element in a copied list at a specific position.

    Args:
        my_list (list): The original list.
        idx (int): The index position of the element to be replaced.
        element: The new element to be placed at the specified index position.

    Returns:
        list: A new list with the element replaced at the specified index position.
             If the index is out of range, the function returns the original list.

    Note:
        This function creates a copy of the original list and modifies the copied list.
        The original list remains unchanged.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
