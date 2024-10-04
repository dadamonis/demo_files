import pandas as pd


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


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
