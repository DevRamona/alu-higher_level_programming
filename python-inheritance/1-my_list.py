#!/usr/bin/python3
""""Defines an inherited list class MyList."""

class MyList(list):
  """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        temp_list = self[:]
        temp_list.sort()
        print("{}".format(temp_list))
