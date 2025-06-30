#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary with integer values.

    Returns:
        key with the highest value or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
