'''
Question 1
[map] Write a Python function square_numbers that takes a list of integers as
input and uses the map function to return a new list containing the square of each
element.
'''
def square_numbers(numbers):
    """
    Compute the square of each element in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing the square of each element in the input list.
    """
    squared_list = list(map(lambda x: x * x, numbers))
    return squared_list

print(square_numbers([1, 2, 3, 4, 5]))  # Output: [1, 4, 9, 16, 25]
print(square_numbers([-2, -1, 0, 1, 2]))  # Output: [4, 1, 0, 1, 4]

'''
Question 2
[filter] Implement a function called filter_prime_numbers that takes a list of
integers as input and uses the filter function to return a new list containing only the
prime numbers
'''
def is_prime(number):
    """
    Check if a number is prime.

    Args:
        number (int): An integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_prime_numbers(numbers):
    """
    Filter out the prime numbers from the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the prime numbers from the input list.

    """
    prime_numbers = list(filter(is_prime, numbers))
    return prime_numbers

print(filter_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  
print(filter_prime_numbers([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
