class MyList(list):
    """
    A class that inherits from list with a method to print sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
