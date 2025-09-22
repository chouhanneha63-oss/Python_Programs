

import time

# Defining the decorator function
def operation_decorator(func, operation):
    def wrapper(a, b):
        print(f"{operation} of {a} and {b}")
        start = time.time()
        result = func(a, b)
        end = time.time()
        print("Result:", result)
        print("Time taken:", end - start)
        return result
    return wrapper

# Defining the basic functions
def add_numbers(a, b):
    return a + b

def sub_numbers(a, b):
    return a - b

# Calling the function with the decorator applied dynamically
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Passing function as an argument to the decorator
add_func = operation_decorator(add_numbers, "Addition")
sub_func = operation_decorator(sub_numbers, "Subtraction")

add_func(a, b)
sub_func(a, b)
