#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load items from JSON file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []  # If the file doesn't exist, start with an empty list

    # Extend the items list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, "add_item.json")
