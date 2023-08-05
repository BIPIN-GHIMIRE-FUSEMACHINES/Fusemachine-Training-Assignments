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


'''
Question 2
[*args] Write a Python function concat_strings that takes any number of strings as
arguments and returns a single concatenated string.
'''
def concat_strings(*args):
    '''
    Concatenate multiple strings into a single string.

    Args:
        *args: Any number of string arguments.

    Returns:
        str: A single string containing all the concatenated strings.
    '''

    return "".join(args)

# Test cases
print(concat_strings("Hello", " ", "fuse","human", "!"))  
print(concat_strings("Working", " ", "with", " ", "*args and **kwargs."))  
print(concat_strings("This", " ", "is", " ", "a", " ", "test."))  
print(concat_strings("One", " ", "two", " ", "three"))  
print(concat_strings("I", " ", "love", " ", "Barcelona", "!"))  

'''
Question 3
[**kwargs] Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items.
'''
def calculate_total_cost(**kwargs):
    """
    Calculate the total cost of items purchased from a store.

    Args:
        **kwargs: Multiple keyword arguments where the key is the item name and the value is the item's price.

    Returns:
        float: The total cost of all items.
    """
    if not kwargs:
        return "No items added."
    
    total_cost = sum(kwargs.values())
    return total_cost

# Test cases
print(calculate_total_cost(item1=10.99, item2=5.49, item3=2.99))  
print(calculate_total_cost(item1=1500.00, item2=812.50, item3=3.3325, item4=6232.75))  
print(calculate_total_cost(item1=1.00, item2=2.00, item3=3.00, item4=4.00))  
print(calculate_total_cost())  