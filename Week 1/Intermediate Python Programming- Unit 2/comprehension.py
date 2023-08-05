'''
Question 1
[list comprehension] Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension.
'''
original_list = ["barcelona", "madrid", "vigo", "city", "united", "miami", "suii", "suiiiiiiiiiiiii"]

# List comprehension to filter strings with more than 5 characters
filtered_list = [word for word in original_list if len(word) > 5]

print(filtered_list)
