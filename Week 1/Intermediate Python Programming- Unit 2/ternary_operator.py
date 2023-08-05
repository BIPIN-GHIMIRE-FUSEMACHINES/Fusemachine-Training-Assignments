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

'''
Question 2
Write a function find_bigger_number that takes three integers as input and uses a
ternary operator to return the larger number. If all numbers are equal, return
"Equal."
'''
def find_bigger_number(num1, num2, num3):
    """
    Find the larger number among three integers.

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.
        num3 (int): The third integer.

    Returns:
        str or int: The larger number or "Equal" if all numbers are equal.
    """
    max_number = max(num1, num2, num3)
    return max_number if max_number != min(num1, num2, num3) else "Equal"

print(find_bigger_number(11, 20, 18))  # Output: 20
print(find_bigger_number(50, 50, 50))    # Output: 'Equal'
print(find_bigger_number(50, 50, 40))    # Output: 50

'''
Question 3
Implement a function called check_prime that takes a positive integer as input and
uses a ternary operator to determine if it's a prime number. Return "Prime" if it is,
otherwise "Not Prime."
'''
def check_prime(number):
    """
    Check if the given positive number is prime.

    Args:
        number (int): The positive integer to be checked.

    Returns:
        str: "Prime" if the number is prime, "Not Prime" otherwise.

    """
    if number < 2:
        return "Not Prime"
    is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    return "Prime" if is_prime else "Not Prime"

print(check_prime(100))   # Output: 'Prime'
print(check_prime(10))  # Output: 'Not Prime'
print(check_prime(13))  # Output: 'Prime'


