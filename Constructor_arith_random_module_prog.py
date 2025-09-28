import random

class Operation:
    def __init__(self):
        
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
        op = ['+', '-', '*', '/','//','%']
    
        self.operator = random.choice(op)

        
        match self.operator:

            case '+':
                result = self.num1 + self.num2

            case '-':
                result = self.num1 - self.num2

            case '*':
                result = self.num1 * self.num2

            case '/':
                 try:
                     result = self.num1 / self.num2

                 except ZeroDivisionError:
                     result = "Error: Division by zero is not allowed."

                 except TypeError:
                     result = "Error: Invalid input types for division."

            case '//':
                result = self.num1 // self.num2

            case '%':
                result = self.num1 % self.num2

            case _:
                result = "Invalid operator"

        print(f"Operator chosen: {self.operator}")
        print(f"Result: {result}")

o = Operation()
