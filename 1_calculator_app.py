# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition,
# subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
method = input("Choose a method (+, -, *, /):")

if method == '+':
    outcome = addition(a, b)
elif method == '-':
    outcome = subtraction(a, b)
elif method == '*':
    outcome = multiplication (a, b)
elif method == '/':
    outcome = division (a, b)
else: 
    print("Error, invalid")

print('Outcome:', outcome)

