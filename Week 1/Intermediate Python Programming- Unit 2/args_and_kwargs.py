'''
[*args] Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases
'''

def sum_of_numbers(*args):
    '''
    Calculate the sum of a given set of numbers.

    Args:
        *args: Any number of integer arguments.

    Returns:
        int: The sum of all the numbers.
    '''
    if not args:
        return "No numbers provided."

    total = sum(args)
    return " + ".join(str(num) for num in args) + f" = {total}"

# Test cases
print(sum_of_numbers(1, 2, 3))  
print(sum_of_numbers(10, 20, 30, 40))  
print(sum_of_numbers(-1, -2, -3, -4, -5))  
print(sum_of_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  
print(sum_of_numbers(100))  
print(sum_of_numbers())  