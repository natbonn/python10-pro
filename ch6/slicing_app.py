"""Slicing lists in Python"""

# sorted by grades
students = ["Άννα","Βασίλης", "Γιώργος", "Δημήτρης", "Ελένη", "Ζωή", "Ηλίας", "Θεοδώρα"]

# top 3 students
top3 = students[:3]    # prints 1 2 3(default slicing 0)
bottom3 = students[-3:] # prints 6 7 8, αρνητικό slicing
middle2 = students[3:5] # prints 4 5

# reverse the list
reversed_students = students[::-1]

print(*reversed_students, sep=", ")