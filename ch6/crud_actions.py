"""CRUD Operations in lists"""


products = ["Milk", "Bread", "Eggs", "Cheese"]

# Traverse
for product in products:
    print(product, sep=" | ")

print()

# enumerate
for index, product in enumerate(products):
    print(f"{index}: {product}", sep=" | ")

# Insert
products.append("Butter")
products.extend(["Yogurt", "Juice"])

# Insert at specific index
products.insert(2, "Cereal")

# Update an element
# The element must be present or error if products[10] in non-existent position
products[1] = "Whole Grain Bread"

# Delete an element by value -- The element must be present or error
products.remove("Eggs")

# Delete with del statement
del products[0]   # IndexError: if products[10] in non-existent position

# Search for an element
if "Cheese" in products:
    print("Cheese is available in the list.")


# safe search with try except
try:
    index = products.index("Butter")
    product = products[index]       # IndexError if the index is out of bounds
    print(f"Butter is at index {index}. ")
    products[index] = "Margarine"   # Update the product at the found index
    products.remove("Butter")       # ValueError if doesnt exist
    print(f"Butter is at index {index}.")
except ValueError:
    print("Butter is not in the list.")
except IndexError:
    print("Index is out of range.")