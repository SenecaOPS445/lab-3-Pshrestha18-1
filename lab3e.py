#!/usr/bin/env python3

# Sample list with mixed types of elements
sample_list = [100, 200, 300, 'six hundred']

def give_list():
    """Returns the entire list."""
    return sample_list

def give_first_item():
    """Returns the first item in the list as a string."""
    return str(sample_list[0])

def give_first_and_last_item():
    """Returns the first and last items in the list."""
    return [sample_list[0], sample_list[-1]]

def give_second_and_third_item():
    """Returns the second and third items in the list."""
    return [sample_list[1], sample_list[2]]

if __name__ == "__main__":
    # You could test the functions here manually, but the unittest framework will test them
    pass
