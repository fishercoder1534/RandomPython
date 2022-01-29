# How to run this program:
# In terminal, run $python3 hello.py

print("Hello world!")

txt = "Viel Glück!"
print("Before encoding, txt: ", txt)
print("After encoding with UTF-8, x: ", txt.encode())  # without specifiying encoding scheme, UTF-8 is used

print("After encoding with ascii, x: ", txt.encode(encoding="ascii",errors="namereplace"))

# for _ in range(10):
#     print("Hello world!")

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
first_col = [row[0] for row in matrix]
print("first_col is: ", first_col)

s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])

var = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# [] means a list, {} means a dict,
# so there is list inside the dict and inside list and inside dict. ^ ^
print("printing out var from nested dict: ", var['k1'][0]['nest_key'][1])

print("Program finished!")
