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

