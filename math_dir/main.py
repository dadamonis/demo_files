import pandas as pd

from arithmetic import (
    add_numbers, 
    subtract_numbers, 
    divide_numbers
    )


def calculate(operation, num1, num2):
    operations = {
        "add": add_numbers,
        "subtract": subtract_numbers,
        "multiply": multiply_numbers,
        "divide": divide_numbers,
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    result = operations[operation](num1, num2)
    return result


try:
    print(calculate("subtract", 5, 3))
except ValueError as e:
    print(e)
