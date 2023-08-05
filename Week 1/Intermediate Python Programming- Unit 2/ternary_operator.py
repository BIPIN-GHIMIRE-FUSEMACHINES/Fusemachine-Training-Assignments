'''
Question 1
Write a Python function called check_odd_even that takes an integer as input and
uses a ternary operator to return "Even" if the number is even, and "Odd" if the
number is odd.
'''
def check_odd_even(number):
    """
    Check if the given number is odd or even.

    Args:
        number (int): An integer to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    """
    return "Even" if number % 2 == 0 else "Odd"

print(check_odd_even(4))  # Output: 'Even'
print(check_odd_even(7))  # Output: 'Odd'
print(check_odd_even(197))  # Output: 'Odd'