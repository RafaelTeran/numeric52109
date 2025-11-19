###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

import math


# We are going to define basic operations as functions

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def cosine(a):
    """Calculate the cosine of a number (in radians)."""
    return math.cos(a)

def sine(a):
    """Calculate the sine of a number (in radians)."""
    return math.sin(a)

def logarithm(a, base=10):
    """Calculate the logarithm of a number with a given base."""
    return math.log(a, base)

def tangent(a):
    """Calculate the tangent of a number (in radians)."""
    return math.tan(a)

# We now define the interface function, which will prompt the user for input
# and call the appropriate function based on the user's input,
# while handling exceptions.

def calculator_interface():
    """Interface for a basic calculator."""
    print("Welcome to the basic calculator!")
    print("Available operations: add, subtract, multiply, divide," \
    " cosine, sine, logarithm, tangent")
    
    while True:
        print("Type 'exit' to quit the calculator.")
        operation = input("Enter operation: ").strip().lower()
        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            # We handle operations with different numbers of arguments
            if operation in ['cosine', 'sine', 'tangent']:
                a = float(input("Enter number (in radians): "))
                b = None
            elif operation == 'logarithm':
                a = float(input("Enter number: "))
                base_input = input("Enter base (default is 10): ").strip()
                b = float(base_input) if base_input else 10
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            if operation == 'add':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)
            else:
                print("Invalid operation. Please try again.")
                print("Available operations: add, subtract, multiply, divide," \
                "cosine, sine, logarithm, tangent")
                continue
            
            if operation in ['cosine', 'sine', 'tangent']:
                print(f"The result of {operation}({a}) is: {result}")
            elif operation == 'logarithm':
                print(f"The result of {operation}({a}, base={b}) is: {result}")
            else:
                print(f"The result of {operation}ing {a} and {b} is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

