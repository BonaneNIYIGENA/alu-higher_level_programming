#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary if it exists.

    Args:
        a_dictionary (dict): The dictionary.
        key (str): The key to delete.

    Returns:
        dict: The dictionary after deletion.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
