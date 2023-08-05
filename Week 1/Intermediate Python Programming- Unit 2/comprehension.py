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