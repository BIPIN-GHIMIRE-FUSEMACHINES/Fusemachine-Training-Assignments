'''
Question 1
[list comprehension] Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension.
'''
original_list = ["barcelona", "madrid", "vigo", "city", "united", "miami", "suii", "suiiiiiiiiiiiii"]

# List comprehension to filter strings with more than 5 characters
filtered_list = [word for word in original_list if len(word) > 5]

print(filtered_list)

'''
Question 2
[list comprehension] Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.
'''

list1 = [1, 2, 3, 4, 5,6,7,8]
list2 = [10, 20, 30, 40, 50,60]

# List comprehension to calculate the product of corresponding elements
product_list = [list1[i] * list2[i] for i in range(min(len(list1), len(list2)))]

print(product_list)

'''
Question 1 - Dictionary
[dictionary comprehension] Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension.
'''
keys = ["name", "age", "city", "gender"]
values = ["Kp Ba", 30, "Nepal", "Male","Yemale"]

# Dictionary comprehension to create the dictionary
my_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

print(my_dict)

'''
Question 2 - dictionary
[dictionary comprehension] Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension.
'''

scores_dict = {
    "Hari": 90,
    "Sita": 75,
    "Gita": 85,
    "Ram": 95,
    "shyam": 78
}

# Dictionary comprehension to filter students with scores more than 80
high_scores_dict = {name: score for name, score in scores_dict.items() if score > 80}

print(high_scores_dict)

'''
Question 1 - Set
[set comprehension] Given a list of numbers, create a set using set
comprehension that contains only unique even numbers.
'''

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Set comprehension to create a set of unique even numbers
even_numbers_set = {num for num in numbers_list if num % 2 == 0}

print(even_numbers_set)



'''
Question 2 - Set
[set comprehension] Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings.
'''

string1 = "fuse"
string2 = "human"

# Set comprehension to create a set of common characters
common_characters_set = {char for char in string1 if char in string2}

print(common_characters_set)

