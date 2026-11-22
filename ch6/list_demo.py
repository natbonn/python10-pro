my_list = [1, 2, 3]
my_list2 = [0] * 5    # repeat 0 * 5 (one list)

# traverse with range (index error, 0 to length-1
for i in range(len(my_list) + 1):   # IndexError: index out of range
    print(my_list[i])

# Traverse print list safe version without IndexError
for item in my_list:
    print(item)

num1 = my_list[1]
num2 = my_list[-1]   # last element of the list

print(*my_list, sep=", ")

my_slice = my_list[1:3]    # one slice of list from index 1 to 2