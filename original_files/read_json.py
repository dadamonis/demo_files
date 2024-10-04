my_list = [
    "import sys\n",
    "\n",
    "\n",
    "def add_numbers(a, b):\n",
    "    return a + b\n",
    "\n",
    "\n",
    "def multiply_numbers(a, b):\n",
    "    return a * b\n",
    "\n",
    "\n",
    "def divide_numbers(a, b):\n",
    "    return a / b\n",
    "\n",
    "\n",
    "def calculate(operation, num1, num2):\n",
    '    if operation == "add":\n',
    "        result = add_numbers(num1, num2)\n",
    '    elif operation == "subtract":\n',
    "        result = subtract_numbers(num1, num2)\n",
    '    elif operation == "multiply":\n',
    "        result = multiply_numbers(num1, num2)\n",
    '    elif operation == "divide":\n',
    "        result = divide_numbers(num1, num2)\n",
    "    else:\n",
    '        print("Invalid operation")\n',
    "\n",
    "    return result\n",
    "\n",
    "\n",
    'print(calculate("subtract", 5, 3))\n',
]

# Join the list into a single string with an empty string as the separator
single_string = "".join(my_list)

# Print the single string
print(single_string)
