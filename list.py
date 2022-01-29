my_list = [1, 2, 3]
print("Before assignment, my_list: {}".format(my_list))

my_list = ["New Item", 2, 3]
print("After assignment, my_list: {}".format(my_list))

list_1 = [3, 4, 5]
my_list.append(list_1)  # this will append list_1 as a whole to my_list
print("after appending, my_list: {}".format(my_list))
my_list.extend(list_1)  # this will concatenate list_1 as a list to list: my_list
print("after extending, my_list: {}".format(my_list))

my_list.pop()  # this will pop off the last element
print("after popping the last element, my_list: {}".format(my_list))

my_list.pop(1)  # this will pop off the second element
print("my_list: {}".format(my_list))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # this is a nested list: a list of lists.
# List comprehension
first_col_list = [row[0] for row in matrix]
print("first_col_list is: ", first_col_list)

squares_list = [row[0] ** 2 for row in matrix]
print("list_2 is: ", squares_list)
