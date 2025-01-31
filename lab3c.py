#!/usr/bin/env python3

def operate(a=None, b=None, operation=None):
    if a is None or b is None or operation is None:
        raise ValueError("Error: function requires two numbers and an operation")

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'