#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A simple program to calculate the factorial of a given non-negative integer.
"""

import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the input integer.

    Raises:
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    return 1 if n == 0 else n * factorial(n - 1)


def main():
    """Main function to test the factorial calculation."""
    try:
        number = int(input("Enter a non-negative integer: "))
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
