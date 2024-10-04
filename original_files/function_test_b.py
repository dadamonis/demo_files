def add_numbers(a: float, b: float) -> float:
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    return a * b

def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(operation: str, num1: float, num2: float) -> float:
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

print(calculate("subtract", 5, 3))
