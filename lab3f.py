#!/usr/bin/env python3

# Initialize the list with the values [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """
    Appends a new item to the list with the value (last item + 1)
    """
    new_value = ordered_list[-1] + 1
    ordered_list.append(new_value)

def remove_items_from_list(ordered_list, items_to_remove):
    """
    Removes specified items from the list.
    Takes two arguments: the list and a list of items to remove.
    """
    for item in items_to_remove:
        if item in ordered_list:
            ordered_list.remove(item)

# Main code execution
if __name__ == '__main__':
    print("Initial list:", my_list)
    
    # Add items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    
    print("List after adding items:", my_list)
    
    # Remove items from the list
    remove_items_from_list(my_list, [1, 5, 6])
    
    print("List after removing items:", my_list)
