#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Return a new list where all occurrences of `search` in `my_list`
    are replaced with `replace`. The original list is not modified.
    """
    return [replace if x == search else x for x in my_list]
