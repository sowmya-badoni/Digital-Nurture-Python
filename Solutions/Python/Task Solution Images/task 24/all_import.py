from math import *

def math_operations(number):

    if number < 0:
        print("Invalid input")
        return

    print(f"Square Root: {sqrt(number)}")
    print(f"Power: {pow(number, 2)}")
    print(f"Value of Pi: {pi}")


math_operations(16)