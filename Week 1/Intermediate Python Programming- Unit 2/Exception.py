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

'''
Question 2
Implement a program that takes user input for a filename, opens the file in read
mode, and displays its contents. Handle the FileNotFoundError and display an error
message if the file is not found.
'''

def read_file_contents(filename):
    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        FileNotFoundError: If the specified file is not found.

    """
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    """
    Main function to read and display the contents of a file.
    """
    filename = input("Enter the filename: ")

    file_contents = read_file_contents(filename)

    if file_contents is not None:
        print(f"Contents of the file '{filename}':")
        print(file_contents)


