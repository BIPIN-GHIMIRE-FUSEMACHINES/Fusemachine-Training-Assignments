'''
Question 1
Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.
'''

def perform_division(num1, num2):
    """
    Perform division between two numbers and return the result.

    This function takes two numbers, num1 and num2, and calculates their division.
    If num2 is equal to zero, a ZeroDivisionError is caught and an error message is printed.

    Parameters:
    num1 (float or int): The dividend.
    num2 (float or int): The divisor.

    Returns:
    float: The result of num1 divided by num2.
    
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

division_result = perform_division(num1, num2)
print(f"The result of {num1} / {num2} is: {division_result}")



