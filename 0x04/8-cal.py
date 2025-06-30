#!/urs/bin/python
"""Write a simple calculator program that does addition, subtraction, 
multiplication, or division based on user input.
Ask the user to enter two numbers and the operation.
Use conditionals and arithmetic operators to compute the result.
Print the result."""

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter the operation (+, -, *, /): ")

# Use conditionals to perform the operation
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
