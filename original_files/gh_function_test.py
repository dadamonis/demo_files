def add_numbers(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Divides the first number by the second. Raises ValueError if the second number is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation: str, num1: float, num2: float) -> float:
    """Performs a calculation based on the given operation."""
    if operation == "add":
        result = add_numbers(num1, num2)
    elif operation == "subtract":
        result = subtract_numbers(num1, num2)
    elif operation == "multiply":
        result = multiply_numbers(num1, num2)
    elif operation == "divide":
        result = divide_numbers(num1, num2)
    else:
        raise ValueError("Invalid operation")

    return result


if __name__ == "__main__":
    # Example usage
    print(calculate("subtract", 5, 3))
