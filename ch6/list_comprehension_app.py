"""List comprehensions in Python

Create a new list from existing list using list comprehension.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# map
doubled_nums = [x * 2 for x in nums]
str_nums = [str(x) for x in nums]

clean_and_lower_names = [name.strip().lower() for name in names]

# Filtering
even_nums = [x for x in nums if x % 2 == 0]

# multiple conditions for filtering - for in / if
even_nums_gt_5 = [x for x in nums if x % 2 == 0 and x > 5]

# if else in list comprehension - mapping not filtering - if else / for in
even_odd = ["even" if x % 2 == 0 else "odd" for x in nums]

# flattening a matrix - like nested for
flattened_matrix = [num for row in matrix for num in row]

# Αντίστοιχα και για άλλες δομές δεδομένων, πχ set, dict, tuples
squared_set = {x ** 2 for x in nums}   # set comprehension, duplicates will be removed
squared_dict = {x: x ** 2 for x in nums}  # dictionary comprehension
lazy = (x * x for x in nums)     # generator expression, lazy evaluation